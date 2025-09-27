import pandas as pd
import numpy as np

tarihler = pd.date_range("2025-09-01", periods=10, freq="D")
satislar = [100,120,90,80,150,200,130,170,160,180]


df = pd.DataFrame({
    "tarih": tarihler,
    "satis": satislar
})

df = df.set_index("tarih")

print("\nYıl:\n",df.index.year)
print("Ay:\n",df.index.month)
print("Haftanın Günü:\n",df.index.day_name(locale="tr_TR"))

print("\nHaftalık toplam satış:\n",df["satis"].resample("W").sum())
print("\Aylık ortalama satış:\n",df["satis"].resample("M").mean())

print("\n5 Eylül ve sonrası satışlar:\n",df.loc["2025-09-05":])