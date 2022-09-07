from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .countries import Countries
from .base import Base


class Provincies(Base):
    __tablename__ = 'provincies'

    id= Column(Integer, primary_key= True)
    country_id= Column(Integer, ForeignKey('countries.id', ondelete= 'CASCADE'))
    name= Column(String, nullable= False)

  
    regencies= relationship('Regencies', back_populates= 'regency', cascade='all, delete')
    regencies= relationship('Districts', back_populates= 'regency', cascade='all, delete')
