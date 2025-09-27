import pandas as pd
import numpy as np

df = pd.read_csv(
    "ogrenciler.csv",
    sep=";",
    encoding="utf-8",
    na_values=["NaN",""]
)

df["kayit_tarihi"] = pd.to_datetime(df["kayit_tarihi"],errors="coerce",dayfirst=True)

df["yas"] = pd.to_numeric(df["yas"],errors="coerce")
df["puan"] = pd.to_numeric(df["puan"],errors="coerce")

print("\nSınıf bazında ortalama puan:")
print(df.groupby("sinif")["puan"].mean())

print("\nSınıf bazında puan istatistikleri:")
print(df.groupby("sinif")["puan"].agg(["count","mean","min","max"]))

print("\nSınıf + yaşa göre ortalama puan:")
print(df.groupby(["sinif","yas"])["puan"].mean())

df["yil"] = df["kayit_tarihi"].dt.year
print(df.groupby("yil")["puan"].mean())