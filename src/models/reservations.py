from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float

from .base import Base

class Reservations(Base):
    __tablename__ = 'reservations'

    id= Column(Integer, primary_key= True)
    guest_id= Column(Integer, ForeignKey('guests.id', ondelete= 'CASCADE'))
    start_time= Column(DateTime, nullable= False)
    end_time= Column(DateTime, nullable= False)
    create_at= Column(DateTime, server_default= datetime.now(), nullable= False)
    last_change= Column(DateTime, nullable= True)
    discount_percent= Column(Float, server_default= 0, nullable= False)
    total_price= Column(Integer, server_default= 0, nullable= False)