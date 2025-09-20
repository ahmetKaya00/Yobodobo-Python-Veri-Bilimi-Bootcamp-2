"""
Satır Açıklaması
Çok Satırlı
"""
#Satır Açıklaması
print("Hello World")

age = 25 #int(sayi)
_pi = 3.14
name = "Ahmet"
is_student = True

print(age,type(age))
print(_pi,type(_pi))
print(name,type(name))
print(is_student,type(is_student))

#Operatörler

a, b = 10, 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(a>b)
print(a<b)
print(a == b)
print(a != b)
print(a >= b)

x, y = True, False

print(x and y)
print(x or y)
print(not x)

text = "Python Programlama"

print(text[0])
print(text[-1])

print(text[0:6])
print(text[7:])
print(text[:-1])

print(text.lower())
print(text.upper())

words = text.split()#['Python','Programlama']
joined = "-".join(words)

print(words)
print(joined)

print("Pro" in text)
print(text.replace("Python","Java"))






