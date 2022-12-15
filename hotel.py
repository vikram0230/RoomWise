from pydantic import BaseModel

class Hotel(BaseModel):
    hotel : list
    is_canceled : list
    lead_time : list
    arrival_date_year : list
    arrival_date_month : list
    arrival_date_week_number : list
    arrival_date_day_of_month : list
    stays_in_weekend_nights : list
    stays_in_week_nights : list
    adults : list
    children : list
    babies : list
    meal : list
    country : list
    market_segment : list
    distribution_channel : list
    is_repeated_guest : list
    previous_cancellations : list
    previous_bookings_not_canceled : list
    reserved_room_type : list
    assigned_room_type : list
    booking_changes : list
    deposit_type : list
    agent : list
    company : list
    days_in_waiting_list : list
    customer_type : list
    adr : list
    required_car_parking_spaces : list
    total_of_special_requests : list
    reservation_status : list
    reservation_status_date : list
