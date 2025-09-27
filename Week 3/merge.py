import pandas as pd

df_ogrenciler = pd.DataFrame({
    "id": [1,2,3,4,5],
    "isim": ["Ayşe","Ali","Zeynep","Can","Ahmet"],
    "sinif": ["A","B","A","B","A"]
})

df_notlar = pd.DataFrame({
    "id":[1,2,3,4,6],
    "puan": [88,77,91,50,75]
})

print(df_ogrenciler)
print(df_notlar)

inner = pd.merge(df_ogrenciler,df_notlar,on="id",how="inner")
print(inner)

left = pd.merge(df_ogrenciler, df_notlar, on="id",how="left")
print(left)

outer = pd.merge(df_ogrenciler,df_notlar, on="id", how="outer")
print(outer)
