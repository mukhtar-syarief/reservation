from datetime import datetime
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

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

def get_current_user(token: str = Depends(oauth2_schema)):
    credential_exception = HTTPException(status_code= status.HTTP_403_FORBIDDEN,
                            detail="Could not Validate credential")
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        token_data = TokenData(**payload)
    except JWTError as e:
        print(e)
        raise credential_exception
    return token_data



