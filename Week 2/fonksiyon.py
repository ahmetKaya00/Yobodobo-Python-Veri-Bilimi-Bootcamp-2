def selamla():
    print("Merhaba")

def selamla(isim="Misafir"):
    print("Merhaba", isim)

def toplama(a,b):
    print("Toplam:", a+b)

def kare_al(sayi):
    return sayi **2

def hesapla(a,b):
    toplam = a + b
    carpim = a * b
    return toplam, carpim

def toplama(*sayilar):
    return sum(sayilar)

def bilgiler(**kwargs):
    print(kwargs)

def kare(x):
    return x**2

kare2 = lambda x:x**2

sayilar = [1,2,3,4,5]

kareler = list(map(lambda x: x**2,sayilar))

isimler = ["Ali","Ayşe","Mehmet"]
yaslar = [25,30,35]

print(len(isimler))
print(list(range(1,6)))
print(list(filter(lambda x: x>25,yaslar)))
print(list(zip(isimler,yaslar)))


print(kareler)

print(kare(2))
print(kare2(2))

bilgiler(ad="Ahmet",yas=15,sehir="Mersin")

print(toplama(1,5,9,7,8))

sonuc = hesapla(3,5)
print(sonuc)
top, car =  hesapla(3,5)
print(top,car)

selamla()
toplama(5,3)

print(kare_al(5))
