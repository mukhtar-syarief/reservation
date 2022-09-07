from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

route = APIRouter(tags= "Login API")

@route.post("")
async def user_login(payload: OAuth2PasswordRequestForm = Depends()):
    raise NotImplementedError
