import pandas as pd

df = pd.read_csv(
    "ogrenciler.csv",
    sep=";",
    encoding="utf-8",
    na_values=["NaN",""]
)

df["kayit_tarihi"] = pd.to_datetime(df["kayit_tarihi"],errors="coerce",dayfirst=True)

#----Sütun Seçme-----
print("\nSadece isim sütunu:\n",df["isim"])
print("\nSadece isim ve puan sütunu:\n",df[["isim", "puan"]])

#----Satır Seçme---
print("\n0.satır (iloc):\n",df.iloc[0])
print("\n1.satır (loc):\n",df.loc[1])

filtre = (df["puan"] >= 80)&(df["sinif"] == "A")
print("\nBaşarılı A sınıfı öğrencileri:\n",df.loc[filtre,["id","isim","puan"]])

mask_isim = df["isim"].str.contains("an",case=False,na=False)
print("\nİsminde 'an' geçen örenciler:\n",df.loc[mask_isim,["isim","puan"]])