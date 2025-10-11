import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

data = {
    "CalismaSaati": [2,3,5,1,4,6,7,8,9,10],
    "Ortalama": [50,55,60,40,65,70,75,80,85,90],
    "GectiMi": [0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

x = df[["CalismaSaati","Ortalama"]]
y = df["GectiMi"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))