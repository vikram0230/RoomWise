from fastapi import APIRouter
from api.models import GuestBooking,GuestReserved
from api.db import conn
from api.schema import serializeDict, serializeList
from bson import ObjectId

user = APIRouter()

@user.get('/all_bookings')
async def get_all_bookings():
    return serializeList(conn.local.user.find())

@user.post('/create_booking')
async def create_booking(guest: GuestBooking):
    # Predict reserve_date
    print(dict(guest))
    conn.local.user.insert_one(dict(guest))
    return serializeList(conn.local.user.find())

@user.delete('/cancel_booking/{id}')
async def cancel_booking(id,guest: GuestBooking):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))