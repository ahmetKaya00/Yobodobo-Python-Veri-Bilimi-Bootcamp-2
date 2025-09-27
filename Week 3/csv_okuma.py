import pandas as pd


df = pd.read_csv(
    "ogrenciler.csv",
    sep=";",
    encoding="utf-8",
    header=0,
    na_values=["NaN",""],
    dtype={
        "id": "Int64",
        "yas": "Int64",
        "sinif": "string"
    }
)

print("Ham DataFrame:\n", df)

df["kayit_tarihi"] = pd.to_datetime(
    df["kayit_tarihi"],
    errors="coerce", #Hatalı tarihleri NaT yap
    dayfirst=True
)

print("\nDönüştürülmüş Bilgi:")
print(df.info())

print("\nEksik Veriler:\n",df.isna().sum())
print("\nKayıt yılı:\n", df["kayit_tarihi"].dt.year)