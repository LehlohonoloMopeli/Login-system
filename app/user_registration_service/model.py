from pydantic import BaseModel

class UserRegistrationModel(BaseModel):
    full_names: str
    surname: str
    id_number: str
    cell_number: str
    email: str
    password: str
    confirm_password: int