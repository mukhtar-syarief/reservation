from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

from .countries import Countries
from .provincies import Provincies
from .regencies import Regencies
from .base import Base


class Districts(Base):
    __tablename__ = 'cities'

    id= Column(Integer, primary_key= True)
    country_id= Column(Integer, nullable= False)
    province_id= Column(Integer, nullable= False)
    regency_id= Column(Integer, nullable= False)
    name= Column(String, nullable= False)
    postal_code= Column(Integer, nullable= False)

    
    __table_args__ = (
        ForeignKeyConstraint(
            [country_id, province_id, regency_id],
            ['countries.id', 'provincies.id', 'regencies.id'], ondelete= 'CASCADE'
        ),
    )