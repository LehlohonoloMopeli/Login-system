from pydantic import BaseModel

class AccountregistrationModel(BaseModel):
    id_number: str
    account_type: str
