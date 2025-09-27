import pandas as pd

s = pd.Series(
    data=[85,90,78],
    index=["Ali","Ayşe","Mehmet"],
    dtype="int64",
    name="puanlar"
)

print("Series:\n", s)
print("\nDeğerler:",s.values)
print("\nİndexler:",s.index)

#Eleman Erişimi

print("\nAyşe'nin puanı:",s["Ayşe"])
print("İlk eleman:", s.iloc[0])
print("Son iki kişi:", s.tail(2))
