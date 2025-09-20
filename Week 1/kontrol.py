x = -1

if x > 0:
    print("pozitif")
elif x == 0:
    print("Sıfır")
else:
    print("Negatif")

age = int(input("Yaşınızı Girin: "))

if age < 18:
    print("Reşit değilsiniz!")
elif age < 65:
    print("Yetişkin")
else:
    print("Emekli")


fruits = ["elma", "armut","çilek"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

count = 0

while count < 3:
    print("Sayaç:",count)
    count += 1


for i in range(5):
    if i == 3:
        break #Döngüyü tamamen kırar
    print("i:",i)

for i in range(5):
    if i == 2:
        continue #Bu turu atla, sonraki tura geç
    print("i:",i)

for i in range(5):
    if i == 2:
        pass #Döngüden çıkarma pas geç
    print("i:",i+1)

for x in range(1,4):
    for y in range(1,4):
        print(x,y)

for i in range(1,6):
    for j in range(1,6):
        print(i*j, end="\t")
    print()

squars = [x**2 for x in range(10)]
print(squars)