from tkinter import CASCADE
from sqlalchemy import Column, Integer, ForeignKey, Boolean

from .guests import Guests
from .reservations import Reservations
from .base import Base

class InvoiceGuest(Base):
    __tablename__ = 'invoices_guest'

    id= Column(Integer, primary_key= True)
    guest_id= Column(Integer, ForeignKey('guests.id', ondelete= 'CASCADE'), nullable= False)
    reservation_id= Column(Integer, ForeignKey('reservations.id'))
    invoice_amount= Column(Integer, nullable= False)
    is_paid= Column(Boolean, server_default= False)
    is_Canceled= Column(Boolean, nullable= True)