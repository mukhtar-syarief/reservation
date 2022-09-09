from fastapi import Depends

from ..models.fields import Field
from ..database import Session, get_db


class FieldRepo:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    async def get_field_by_id(self, field_id: int):
        return self.db.query(Field).filter(Field.id == field_id).first()
