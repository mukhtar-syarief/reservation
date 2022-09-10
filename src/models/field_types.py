from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

from .base import Base


class FieldTypeResponse(BaseModel):
    name: str

    class Config:
        orm_mode= True

class FieldTypes(Base):
    __tablename__ = 'field_types'

    id= Column(Integer, primary_key= True)
    name= Column(String, nullable= False)