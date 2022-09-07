from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

class Countries(Base):
    __tablename__ = 'countries'

    id= Column(Integer, primary_key= True)
    name= Column(String, unique= True)

    regencies= relationship('Provincies', back_populates= 'country', cascade='all, delete')
    regencies= relationship('Regencies', back_populates= 'country', cascade='all, delete')
    regencies= relationship('Districts', back_populates= 'country', cascade='all, delete')