from sqlalchemy import Column, Integer, String

from .base import Base


class FieldTypes(Base):
    __tablename__ = 'field_types'

    id= Column(Integer, primary_key= True)
    name= Column(String, nullable= False)