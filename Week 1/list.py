fruits = ["elma","muz","çilek"]
print(fruits[0])
fruits.append("karpuz")
print(fruits)
fruits[1] = "armut"
print(fruits)

colors = ("kırmızı","yeşil","mavi")
print(colors[0])
#colors.append("Ahmet") HATA VERİR
#colors[1] = "mor" HATA VERİR
print(colors)

person = {
    "name": "Ahmet",
    "age": 38,
    "is_student": False
}

print(person["name"])
person["age"] = 25
person["city"] = "İstanbul"
print(person)

numbers = {1,2,3,3,4}
print(numbers)

numbers.add(5)
numbers.remove(2)
print(numbers)

set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)


