from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import joblib
from preprocessing import Preprocessing
import pandas as pd
import json
from hotel import Hotel

app = FastAPI()
pickle_in = open("m1_pipeline.pkl","rb")
classifier = pickle.load(pickle_in)

@app.get('/')
async def index():
    return {'message':'hello world'}

@app.get('/predict')
async def predict(data:dict):
    df = pd.DataFrame(data, columns=data.keys())
    df = df.infer_objects()
    processed_data = Preprocessing().preprocess(df)
    prediction = classifier.predict(processed_data)
    return {"predict": int(prediction[0])}
    df['will_cancel'] = int(prediction[0])


def __init__():
    uvicorn.run(app, host='127.0.0.1', port=8000)


# uvicorn main:app --reload

