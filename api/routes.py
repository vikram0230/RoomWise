import os
import pickle
import pandas as pd
from api.db import conn
from pathlib import Path
from bson import ObjectId
from fastapi import APIRouter
from api.feature_extractor import FeatureExtractor
from api.models import GuestBooking,GuestReserved
from api.schema import serializeDict, serializeList

user = APIRouter()

def get_pickle_path():
    os.getcwd()
    current_directory = Path(os.getcwd())
    pkl_path = os.path.join(current_directory, 'pickle_files')
    return pkl_path

def load_pkl_model(filename):
    pickle_path = get_pickle_path()
    pkl_file = os.path.join(pickle_path, filename + '.pkl')
    model = pickle.load(open(pkl_file,'rb'))
    return model

fx = FeatureExtractor()
model_1 = load_pkl_model("model_1_svc")
model_2 = load_pkl_model("model_2_rf")

@user.get('/all_bookings')
async def get_all_bookings():
    return serializeList(conn.local.user.find())

@user.post('/create_booking')
async def create_booking(guest: GuestBooking):
    guest_data = dict(guest)
    del guest_data['name']
    del guest_data['reserve_date']

    df = pd.DataFrame([guest_data])
    df_transformed = fx.transform(df)

    pred_1 = model_1.predict(df_transformed)
    print('Model 1 Prediction: ',pred_1)
    pred_2 = model_2.predict(df_transformed)
    print('Model 2 Prediction:', pred_2)

    # Calculates the lead time for cancellation
    if pred_1[0] == 1:   
        date_object = datetime.strptime(guest_data['arrival_date'], '%Y-%m-%d').date()
        guest_data['reserve_date'] = (date_object + timedelta(days=-int(pred_2))).strftime('%Y-%m-%d')
    # If no cancellation is predicted, the room is reserved for the guest
    else:
        guest_data['reserve_date'] = guest_data['booking_date']

    print(guest_data)
    guest.reserve_date = guest_data['reserve_date']
        
    conn.local.user.insert_one(dict(guest))
    return serializeList(conn.local.user.find())

@user.delete('/cancel_booking/{id}')
async def cancel_booking(id,guest: GuestBooking):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))