from fastapi import FastAPI
from app.model import Iris
import joblib
import pandas as pd

app = FastAPI()

# carica modello (con pipeline inclusa)
mlr_model= joblib.load("models/mlr_model_pipe.joblib")
knn_model = joblib.load("models/mlr_model_pipe.joblib")


# -------------------------
# TEST ENDPOINT
# -------------------------

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


# -------------------------
# PREDICTION ENDPOINT
# -------------------------
@app.post("/predict/mlr")
def predict(data: Iris):

    # converte input in DataFrame
    df = pd.DataFrame([data.model_dump() if hasattr(data, "model_dump") else data.dict()])

    # prediction
    pred = mlr_model.predict(X)[0]

    return {
        "Category": pred
    }

@app.post("/predict/knn")
def predict(data: Iris):

    # converte input in DataFrame
    df = pd.DataFrame([data.model_dump() if hasattr(data, "model_dump") else data.dict()])

    # prediction
    pred = knn_model.predict(X)[0]

    return {
        "Category": pred
    }
    
# TO RUN ON TERMINAL DO : uvicorn app.main:app --reload

