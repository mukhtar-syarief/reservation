from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .payment_checks import PaymentCheck
from .base import Base


class Payment(Base):
    __tablename__ = 'payments'

    id= Column(Integer, primary_key= True)
    check_id= Column(Integer, ForeignKey('payment_checks.id'))
    is_paid= Column(Boolean, server_default= False)

    check= relationship('PayamentCheck', back_populates= 'payment')