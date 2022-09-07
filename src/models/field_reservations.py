from sqlalchemy import Column, Integer, ForeignKey

from .reservations import Reservations
from .base import Base


class FieldReservations(Base):
    __tablename__ = 'field_reservations'

    id= Column(Integer, primary_key= True)
    reservation_id= Column(Integer, ForeignKey('reservations.id', ondelete= 'CASCADE'))
    price= Column(Integer, server_default= 0, nullable= False)