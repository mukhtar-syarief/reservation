from sqlalchemy import Column, Integer, ForeignKey
from pydantic import BaseModel

from .reservations import Reservations
from .fields import Field, FieldResponse
from .base import Base

class FieldResponse(BaseModel):
    field: FieldResponse
    price: int

    class Config:
        orm_mode= True


class FieldReservations(Base):
    __tablename__ = 'field_reservations'

    id= Column(Integer, primary_key= True)
    field_id= Column(Integer, ForeignKey('fields.id'))
    reservation_id= Column(Integer, ForeignKey('reservations.id', ondelete= 'CASCADE'))
    price= Column(Integer, server_default= 0, nullable= False)