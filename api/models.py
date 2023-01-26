from pydantic import BaseModel

class GuestBooking(BaseModel):
    name:str
    booking_date:str
    arrival_date:str
    departure_date:str
    adult:int
    children:int
    babies:int
    meal:str
    country:str
    booking_type:str
    room_type:str
    car_parking:int
    special_request:int
    reserve_date:str


class GuestReserved(BaseModel):
    name:str
    booking_date:str
    arrival_date:str
    departure_date:str
    adult:int
    children:int
    babies:int
    meal:str
    country:str
    booking_type:str
    room_type:str
    car_parking:int
    special_request:int