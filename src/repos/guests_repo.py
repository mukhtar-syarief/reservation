from datetime import datetime
from fastapi import Depends
from pydantic import BaseModel

from ..models.guests import Guests
from ..database import Session, get_db

class GuestResp(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    address: str
    create_at: datetime

    class Config:
        orm_mode= True


class GuestsRepo:

    def __init__(self, db: Session = Depends(get_db)):
        self.db= db

    async def get_guest_by_id(self, guest_id: int):
        guest = self.db.query(Guests).filter(Guests.id == guest_id).first()
        return GuestResp(**guest)

    async def get_guest_by_username(self, username: str):
        return self.db.query(Guests).filter(Guests.username == username).first()