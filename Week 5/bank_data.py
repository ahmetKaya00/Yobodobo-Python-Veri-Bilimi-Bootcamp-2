import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
    precision_recall_curve
)

plt.rcParams["figure.figsize"] = (6,4)

path = "bank-additional-full.csv"
df = pd.read_csv(path, sep=";")

print(df.shape)
print(df.head())
print(df.dtypes)

na_counts = df.isna().sum().sort_values(ascending=False)
print(na_counts.head(10))

obj_cols = [c for c in df.columns if df[c].dtype == "object"]
unknown_count = {c: int((df[c] == "unknown").sum()) for c in obj_cols}
unknown_sorted = sorted(unknown_count.items(),key=lambda x:x[1],reverse=True)

for col, cnt in unknown_sorted[:10]:
    print(f"{col:20s} -> {cnt}")

target_counts = df["y"].value_counts()
target_ratio = (target_counts / len(df) * 100).round(2)
print(pd.DataFrame({"count": target_counts, "ratio_%": target_ratio}))

target_counts.plot(kind="bar")
plt.title("Hedef (y) Dagilimi")
plt.xlabel("Sinif")
plt.ylabel("adet")
plt.tight_layout()
plt.show()

y = df["y"].map({"no": 0, "yes": 1})

x_full = df.drop(columns=["y"])

numeric_features = [
    "age","duration","campaign","pdays","previous",
    "emp.var.rate","cons.price.idx","cons.conf.idx","euribor3m","nr.employed"
]

categorial_features = [c for c in x_full.columns if c not in numeric_features]

print(numeric_features)
print(len(categorial_features))

numeric_transformer = StandardScaler()
categorial_transformer = OneHotEncoder(handle_unknown="ignore")

preprocesseor_full = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer,numeric_features),
        ("cat", categorial_transformer,categorial_features)
    ]
)

log_reg = LogisticRegression(max_iter=1000,C=1.0,solver="lbfgs")

pipe_full = Pipeline(steps=[
    ("prep",preprocesseor_full),
    ("clf", log_reg)
])

x_train_f, x_test_f, y_train_f, y_test_f = train_test_split(x_full,y,test_size=0.2,random_state=42)

pipe_full.fit(x_train_f,y_train_f)

y_pred_f = pipe_full.predict(x_test_f)
y_probe_f = pipe_full.predict_proba(x_test_f)[:,1]

print("Accuracy:", (y_pred_f == y_test_f).mean().round(4))
print("ROC-AUC:",roc_auc_score(y_test_f,y_probe_f).round(4))
print("\nClassification Repprt:\n", classification_report(y_test_f,y_pred_f,target_names=["no","yes"]))


numeric_wo_dur = [c for c in numeric_features if c != "duration"]
cat_wo_dur = [c for c in x_full.columns if c not in numeric_wo_dur and c != "duration"]

preprocesseor_wo_full = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(),numeric_wo_dur),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_wo_dur)
    ]
)

log_reg_bal =  LogisticRegression(max_iter=1000,C=1.0,solver="lbfgs", class_weight="balanced")

pipe_wo_dur = Pipeline(steps=[
    ("prep",preprocesseor_wo_full),
    ("clf", log_reg_bal)
])

x_wo_dur = df.drop(columns=["y","duration"])

x_train_b, x_test_b, y_train_b, y_test_b = train_test_split(x_wo_dur,y,test_size=0.2,stratify=y,random_state=42)

pipe_wo_dur.fit(x_train_b,y_train_b)

y_pred_b = pipe_wo_dur.predict(x_test_b)
y_probe_b = pipe_wo_dur.predict_proba(x_test_b)[:,1]

print("Accuracy:", (y_pred_b == y_test_b).mean().round(4))
print("ROC-AUC:",roc_auc_score(y_test_b,y_probe_b).round(4))
print("\nClassification Repprt:\n", classification_report(y_test_b,y_pred_b,target_names=["no","yes"]))

cm_b = confusion_matrix(y_test_b, y_pred_b)
print(cm_b)


threshold = 0.35
y_pred_thresh = (y_probe_b >= threshold).astype(int)

print("Accuracy:", (y_pred_thresh == y_test_b).mean().round(4))
print("ROC-AUC:",roc_auc_score(y_test_b,y_probe_b).round(4))
print("\nClassification Repprt:\n", classification_report(y_test_b,y_pred_thresh,target_names=["no","yes"]))