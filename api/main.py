from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List
import joblib


app = FastAPI()


class Data(BaseModel):
    data: List[float]


# loading the model (model.pkl)
path = "../models/best_model.pkl"
model = joblib.load(path)


@app.post("/predict")
def predict(data: Data = Body(...)):
    print(data)
    if len(data.data) != 164:
        return {"error": "invalid data"}
    prediction = model.predict([data.data])
    return {"prediction": prediction[0]}

