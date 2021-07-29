from fastapi import APIRouter
from .model import AccountregistrationModel
from .service import AccountRegistration

router = APIRouter()

@router.post("/register_account", tags=["Account Registration"])
async def account_registration_api(data: AccountregistrationModel):
    return AccountRegistration(data).register_account()
