from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel


route = APIRouter(tags= "Login API")


class LoginPayload(BaseModel):
    username: str
    password: str


@route.post("")
async def user_login(payload: LoginPayload):
    raise NotImplementedError
