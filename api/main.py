from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List
import joblib
import csv


app = FastAPI()


with open('xtest.csv', 'r') as f:
    x = list(csv.reader(f))[0]


class Data(BaseModel):
    data: List[float]

    model_config = {
        "json_schema_extra": {
            "example": {
                "data": [float(i) for i in x]
            }
        }
    }


class Prediction(BaseModel):
    prediction: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "prediction": 4.778
            }
        }
    }


path = "../models/best_model.pkl"
model = joblib.load(path)


@app.post("/predict")
def predict(data: Data = Body(...)) -> Prediction:
    '''
    This function takes in a list of 164 features and returns a prediction

    We assume that the data is already preprocessed
    '''
    if len(data.data) != 164:
        return {"error": "data must be a list of 164 features"}
    prediction = model.predict([data.data])
    return {"prediction": prediction[0]}

