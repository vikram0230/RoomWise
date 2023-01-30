from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import joblib
from preprocessing import Preprocessor
import pandas as pd
import json
from hotel import Hotel

app = FastAPI()

def load_model(filename):
    pickle_in = open(filename,"rb")
    model = pickle.load(pickle_in)
    return model

feature_extractor = load_model('feature_extractor.pkl')
model_1 = load_model("model_1_svc.pkl")
model_2 = load_model("model_2_rf.pkl")

@app.get('/')
async def index():
    return {'message':'hello world'}

@app.get('/predict')
async def predict(data:dict):
    df = pd.DataFrame(data, columns=data.keys())
    df = df.infer_objects()
    processed_data = preprocessor.preprocess(df)
    model_1_pred = model_1.predict(processed_data)
    print(model_1_pred)
    return {"cancel_pred": int(model_1_pred[0])}
    # df['will_cancel'] = int(prediction[0])


def __init__():
    uvicorn.run(app, host='127.0.0.1', port=8000)


# uvicorn main:app --reload

