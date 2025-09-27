import pandas as pd

df = pd.DataFrame(
    data={
        "isim": ["Ali","Ayşe","Mehmet"],
        "yas": [20,21,19],
        "puan": [85,90,78]
    },
    columns=["isim","yas","puan"]
)

print("DataFrame:\n",df)

print(df.info())
print("\n İlk iki satır:\n", df.head(2))
print("\n Sadece isim sutunu:\n", df["isim"])

print("\n0. satır (iloc):\n", df.iloc[0])
print("\n1. satır (loc):\n", df.loc[1])

