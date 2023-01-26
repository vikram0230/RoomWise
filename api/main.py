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
preprocessor = Preprocessor()

model_1 = preprocessor.load_model("model_1_....pkl")
model_2 = preprocessor.load_model("model_2_....pkl")

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

