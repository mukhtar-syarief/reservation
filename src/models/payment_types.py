from sqlalchemy import Column, Integer, String

from .base import Base


class PaymentType(Base):
    __tablename__ = 'payment_types'

    id= Column(Integer, primary_key= True)
    name= Column(String, nullable= False)