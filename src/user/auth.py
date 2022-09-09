from datetime import datetime
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from ..database import Session, get_db
from ..repos.guests_repo import GuestsRepo

SECRET_KEY = 'test'
ALGORITHM = 'sha256'

oauth2_schema = OAuth2PasswordBearer(tokenUrl= '/login')

class TokenData(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    address: str
    create_at: datetime


async def get_token_data(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    guest_repo= GuestsRepo(db)
    credential_exception = HTTPException(status_code= status.HTTP_403_FORBIDDEN,
                            detail="Could not Validate credential")
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        guest = guest_repo.get_guest_by_id(payload['guest_id'])
        token_data = TokenData(**guest)
    except JWTError as e:
        print(e)
        raise credential_exception
    return token_data

async def get_token_string(token: str = Depends(oauth2_schema)):
    return token


