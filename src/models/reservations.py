from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric
from sqlalchemy.sql import func
from pydantic import BaseModel

from .guests import Guests
from .base import Base


class ReservationResponse(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    discount: Numeric
    total_price: Integer

    class Config:
        orm_mode= True


class Reservations(Base):
    __tablename__ = 'reservations'

    id= Column(Integer, primary_key= True)
    guest_id= Column(Integer, ForeignKey('guests.id', ondelete= 'CASCADE'))
    start_time= Column(DateTime, nullable= False)
    end_time= Column(DateTime, nullable= False)
    create_at= Column(DateTime, server_default= func.now(), nullable= False)
    last_change= Column(DateTime, nullable= True)
    discount_percent= Column(Numeric, server_default= 0, nullable= False)
    total_price= Column(Integer, server_default= 0, nullable= False)