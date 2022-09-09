from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class TrainingCentre(Base):
    __tablename__ = 'training_centre'

    id= Column(Integer, primary_key= True)
    district_id= Column(Integer, ForeignKey('districts.id', ondelete= 'SET NULL'))
    name= Column(String, nullable= False)
    description= Column(String, nullable= True)
    detail_address= Column(String, nullable= True)
    is_active= Column(Boolean, server_default= True, nullable= False)


    address = relationship('Districts')
    