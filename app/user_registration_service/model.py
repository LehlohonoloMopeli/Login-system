from pydantic import BaseModel

class UserRegistrationModel(BaseModel):
    full_names: str
    surname: str
    email: str
    password: str
    confirm_password: str