import os

import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier

os.makedirs("models", exist_ok=True)

with open("params.yaml") as f:
    params = yaml.safe_load(f)

train = pd.read_csv("data/processed/train.csv")
X_train = train.drop(columns=["is_fraud", "transaction_id", "merchant"])
X_train = pd.get_dummies(X_train, columns=["category"])
y_train = train["is_fraud"]

model = RandomForestClassifier(
    n_estimators=params["n_estimators"],
    random_state=42,
)
model.fit(X_train, y_train)
joblib.dump(model, "models/model.pkl")

print(f"Trained RandomForestClassifier with n_estimators={params['n_estimators']}")