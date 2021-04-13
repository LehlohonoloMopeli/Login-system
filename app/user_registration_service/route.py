from fastapi import APIRouter
from .model import UserRegistrationModel
from .service import UserRegistration
import logging

router = APIRouter()

logging.basicConfig(filename="server.log", encoding="utf-8", level=logging.DEBUG)

@router.post("/register_user", tags=["User Registration"])
async def user_registration_api(registration: UserRegistrationModel):
    return UserRegistration(registration).register_user()
