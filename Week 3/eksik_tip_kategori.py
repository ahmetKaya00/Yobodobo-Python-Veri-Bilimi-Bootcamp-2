import pandas as pd
import numpy as np

df = pd.read_csv(
    "ogrenciler.csv",
    sep=";",
    encoding="utf-8",
    na_values=["NaN",""]
)

df["kayit_tarihi"] = pd.to_datetime(df["kayit_tarihi"],errors="coerce",dayfirst=True)


print("===Başlangıç Durumu===")
print(df)

print("\nTipler:\n", df.dtypes)
print("\nEksik Sayılar:\n", df.isna().sum())

for col in ["yas","puan"]:
    df[col] = pd.to_numeric(df[col],errors="coerce")

puan_medyan = df["puan"].median()
df["puan"] = df["puan"].fillna(puan_medyan)

df["yas"] = df.groupby("sinif")["yas"].transform(lambda s:s.fillna(s.median()))

df["sinif"] = df["sinif"].astype("category")

df["yas"] = df["yas"].astype("Int64")

print("\n===Dönüşümler Sonrası===")
print(df)
print("\nTipler:\n", df.dtypes)
print("\nEksik Sayılar:\n", df.isna().sum())

df_kritik = df.dropna(subset=["kayit_tarihi"])
print(df_kritik)

df_sorted = df.sort_values("kayit_tarihi")
df_sorted["son_bilinen_puan"] = df_sorted["puan"].ffill()
print(df_sorted[["isim","kayit_tarihi","puan","son_bilinen_puan"]])
