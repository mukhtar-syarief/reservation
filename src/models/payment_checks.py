from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from .payment_types import PaymentType
from .base import Base


class PaymentCheck(Base):
    __tablename__ = 'payment_checks'

    id= Column(Integer, primary_key= True)
    pte_id= Column(Integer, ForeignKey('payment_types.id'))
    evident= Column(String, nullable= False)
    verify= Column(Boolean, server_default= False, nullable= False)

    payment_type= relationship('PaymentType')