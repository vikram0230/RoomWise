from pydantic import BaseModel

class GuestBooking(BaseModel):
    name:str
    booking_date:str
    arrival_date:str
    departure_date:str
    adults:int
    children:int
    babies:int
    meal:str
    country:str
    market_segment:str
    reserved_room_type:str
    required_car_parking_spaces:int
    total_of_special_requests:int
    reserve_date:str


class GuestReserved(BaseModel):
    name:str
    booking_date:str
    arrival_date:str
    departure_date:str
    adults:int
    children:int
    babies:int
    meal:str
    country:str
    market_segment:str
    reserved_room_type:str
    required_car_parking_spaces:int
    total_of_special_requests:int