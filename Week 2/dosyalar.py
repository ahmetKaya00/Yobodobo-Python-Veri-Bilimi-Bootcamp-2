with open("deneme.txt","r",encoding="utf-8") as f:
    icerik = f.read()
    print(icerik)

with open("deneme.txt","r",encoding="utf-8") as f:
    for satir in f:
        print(satir.strip())

with open("notlar.txt","w",encoding="utf-8") as f:
    f.write("Merhaba\n")
    f.write("Python\n")

with open("notlar.txt","a",encoding="utf-8") as f:
    f.write("Selamlar\n")

ogrenciler = ["Ali,85\n","Ayşe,90\n","Mehmet,70\n"]
with open("ogrtenciler.txt","w",encoding="utf-8") as f:
    f.writelines(ogrenciler)
