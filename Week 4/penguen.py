import os
from pathlib import Path
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)

print(df.head())

print(df.info())

print(df.isna().sum())

df['sex'] = df['sex'].fillna(df['sex'].mode()[0])
num_cols = ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

print(df.isna().sum())

species_weight = df.groupby("species")['body_mass_g'].mean()
print(species_weight)

plt.hist(df['body_mass_g'],bins=20,edgecolor='black')
plt.title("Penguen Vucut Agirligi Dagilimi")
plt.xlabel("Vucut Agirligi")
plt.ylabel("Adet")
plt.show()

df.boxplot(column="flipper_length_mm", by="species", grid=False)
plt.title("Turlere Gore Yuzgec Uzunlugu Dagilimi")
plt.xlabel("Tur")
plt.ylabel("Yuzgec Uzunlugu")
plt.show()

pivot_table = df.pivot_table(
    values="body_mass_g",
    index="species",
    columns="sex",
    aggfunc="mean"
)
print(pivot_table)

plt.figure(figsize=(8,6))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(
        subset['bill_length_mm'],
        subset['flipper_length_mm'],
        label=species,
        alpha=0.7
    )

plt.title("Gaga uzunlugu vs Yuzgec Uzunlugu")
plt.xlabel("Gaga Uzunlugu")
plt.ylabel("Yuzgec Uzunlugu")
plt.legend()
plt.show()