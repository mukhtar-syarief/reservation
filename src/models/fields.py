from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

from .field_types import FieldTypes
from .base import Base

class Field(Base):
    __tablename__ = 'fields'

    id= Column(Integer, primary_key= True)
    training_centre_id= Column(Integer, nullable= False)
    type_id= Column(Integer, nullable= True)
    name= Column(String, nullable= False)
    description= Column(String, nullable= True)
    current_price= Column(Integer, server_default= 0,nullable= False)


    __table_args__= (
        ForeignKeyConstraint(
            [training_centre_id, type_id],
            [ 'training_centre.id','field_types.id'], ondelete= 'CASCADE'
        )
    )
