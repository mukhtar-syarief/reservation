from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from .countries import Countries
from .provincies import Provincies
from .base import Base


class Regencies(Base):
    __tablename__ = 'regencies'

    id= Column(Integer, primary_key= True)
    country_id= Column(Integer, nullable= False)
    province_id= Column(Integer, nullable= False)
    name= Column(String, nullable= False)


    __table_args__ = (
        ForeignKeyConstraint(
            [country_id, province_id],
            ['provincies.id', 'provincies.country_id'], ondelete= 'CASCADE'
        ),
    )
    
    districts= relationship('Districts', back_populates= 'regency', cascade='all, delete')