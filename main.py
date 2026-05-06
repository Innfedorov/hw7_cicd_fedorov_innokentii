from fastapi import FastAPI
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os

app = FastAPI()

# фейковая модель (просто заглушка)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit([[0,0,0,0]], [0])  # dummy train

version = os.getenv("MODEL_VERSION", "v1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "version": version}

@app.post("/predict")
def predict(features: list[float]):
    pred = model.predict([features])[0]
    return {"prediction": int(pred), "version": version}
