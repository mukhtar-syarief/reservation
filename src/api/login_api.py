from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from ..repos.guests_repo import GuestsRepo, GuestResp
from ..helper.hash_verify_password import hashing_password, verify_password
from ..database import Session, get_db


router = APIRouter(tags= "Login API")


class LoginPayload(BaseModel):
    username: str
    password: str


@router.post("")
async def user_login(
    payload: LoginPayload,
    db: Session = Depends(get_db),
    guests: GuestsRepo = Depends(GuestsRepo)):
    
    guest = await guests.get_guest_by_username(payload.username)
    if not guests:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
        detail = "User Not Found.!")

    hash_password = await hashing_password(payload.password)
    if not await verify_password(hash_password, guest.password):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
        detail = "Worng Password.!")
        
    return guest
