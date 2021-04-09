from fastapi import APIRouter
from .model import LoginModel
from .service import Login
import logging

router = APIRouter()

logging.basicConfig(filename="server.log", encoding="utf-8", level=logging.DEBUG)

@router.post("/login", tags=["Login"])
async def login_api(loginDetails: LoginModel):
    return Login(loginDetails).login()
