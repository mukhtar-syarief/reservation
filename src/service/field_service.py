from fastapi import Depends
from pydantic import BaseModel

from ..models.fields import Field
from ..repos.field_repo import FieldRepo
from ..database import Session, get_db


class FieldUpdatePayload(BaseModel):
    name: str
    desc: str
    current_price: int


class FieldService:
    field_repo: FieldRepo

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db
        self.field_repo= FieldRepo(self.db)

    async def update_field(self, field_id: int, payload: FieldUpdatePayload):
        field: Field = await self.field_repo.get_field_by_id(field_id)
        field.name = payload.name
        field.description = payload.desc
        field.current_price = payload.current_price
        self.db.commit()