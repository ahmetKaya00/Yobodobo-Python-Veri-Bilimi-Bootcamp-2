import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])

print("a:", a, "ndim:", a.ndim, "shape:", a.shape,"dtype:",a.dtype)
print("b:", b, "ndim:", b.ndim, "shape:", b.shape,"dtype:",b.dtype)

x = np.arange(0,10,2)
y = np.linspace(0,1,5)
z = np.zeros((2,3))
o = np.ones((2,2))
I = np.eye(3)
rng = np.random.default_rng(42)
r = rng.normal(0,1,(2,3))

print(x, y, "\n",z, "\n",o,"\n",I,"\n",r)

A = np.arange(1,13).reshape(3,4)

print(A)
print(A[0,0])
print(A[:, 1])
print(A[1, :2])
print(A.T)

a = np.array([1,2,3])
b = np.array([10,20,30])
print(a+b)
print(a*b)
print(np.sqrt(b))

A = np.ones((3,4))
b = np.array([1,2,3,4])
print(A+b)

M = np.arange(1,13).reshape(3,4)

print(M)
print("Tüm elemanların toplamı:", M.sum())
print("Sütun bazında toplam:", M.sum(axis=0))
print("Satır bazında toplam:", M.sum(axis=1))
print("Ortalama:", M.mean())
print("Standart Sapma:",M.std())

x = np.arange(10)
print(x[x%2 == 0])

arr = np.array([10,20,30,40,50])
idx = [0,2,4]
print(arr[idx])

data = np.arange(1,10).reshape(3,3)
np.savetxt("mat.csv",data,delimiter=",",fmt="%d")

loaded = np.loadtxt("mat.csv",delimiter=",",dtype=int)
print(loaded)


