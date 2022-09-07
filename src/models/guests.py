from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class Guests(Base):
    __tablename__ = 'guests'

    id= Column(Integer, primary_key= True)
    name= Column(String, nullable= False)
    username= Column(String, unique= True, nullable= False)
    password= Column(String, nullable= False)
    email= Column(String, unique= True, nullable=False)
    phone= Column(String, nullable= False)
    address= Column(String, nullable= False)
    create_at= Column(DateTime, server_default= datetime.now())

    invoice= relationship('InvoiceGuest', cascade= 'all, delete')
    reservation= relationship('Reservations', cascade= 'all, delete')