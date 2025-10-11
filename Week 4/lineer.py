import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

data = {
    "study_hours": [1,2,3,4,5,6,7,8,9,10],
    "exam_score": [35,40,50,55,65,70,75,80,85,90]
}

df = pd.DataFrame(data)

print(df)

x = df[['study_hours']]
y = df['exam_score']

model = LinearRegression()

model.fit(x,y)

print("Intercept (a):", model.intercept_)
print("Eğim:", model.coef_[0])

print("7 saat çalısan ogrencinin tahmini notu:", model.predict([[7]])[0])

y_pred = model.predict(x)

plt.scatter(x,y,color="blue",label="Gercek Veriler")
plt.plot(x,y_pred,color="red",label="Regresyon Dogrusu")

plt.xlabel("Calisma Saati")
plt.ylabel("Sınav Notu")
plt.title("Lineer Regresyon")
plt.legend()
plt.show()

y_true = y
y_pred = model.predict(x)

r2 = r2_score(y_true,y_pred)

mae = mean_absolute_error(y_true,y_pred)

mse = mean_squared_error(y_true,y_pred)

rmse = np.sqrt(mse)

print(r2)
print(mae)
print(mse)
print(rmse)