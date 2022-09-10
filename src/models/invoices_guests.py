from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from .guests import Guests, GuestResponse
from .reservations import Reservations, ReservationResponse
from .payment import Payment
from .base import Base


class InvoiceGuestResponse(BaseModel):
    id: int
    guest: GuestResponse
    reservation: ReservationResponse

    class Config:
        orm_mode= True


class InvoiceGuest(Base):
    __tablename__ = 'invoices_guest'

    id= Column(Integer, primary_key= True)
    guest_id= Column(Integer, ForeignKey('guests.id', ondelete= 'CASCADE'), nullable= False)
    reservation_id= Column(Integer, ForeignKey('reservations.id'))
    payment_id= Column(Integer, ForeignKey('payments.id'))
    is_paid= Column(Boolean, server_default= False, nullable= False)
    is_Canceled= Column(Boolean, nullable= True)

    payment= relationship('Payment', back_populates= 'invoice')