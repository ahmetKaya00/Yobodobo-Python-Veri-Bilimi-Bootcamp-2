import pandas as pd

df = pd.DataFrame({
    "isim": ["Ayse","Ali","Zeynep","Can","Deniz","Mert"],
    "sinif": ["A","B","A","B","A","B"],
    "yil": [2023,2023,2024,2023,2024,2024],
    "puan": [88,77,91,65,85,72]
})
print(df)
pivot = df.pivot_table(
    values="puan",
    index="sinif",
    columns="yil",
    aggfunc="mean",
    fill_value=0
)
print(pivot)

pivot_multi = df.pivot_table(
    values="puan",
    index="sinif",
    columns="yil",
    aggfunc=["mean","max","count"],
    fill_value=0
)
print(pivot_multi)

crosstab = pd.crosstab(df["sinif"],df["yil"])
print(crosstab)