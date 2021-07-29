from app.database_model import Session
from app.database_model.user import User
from app.user_login_service.validators.validate_user import validate_email_existance
from app.user_login_service.validators.validate_user import validate_password
from .model import LoginModel

#Responses
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class Login():
    
    def __init__(self, inputs: LoginModel):
        self.__inputs = inputs
        self.session = Session()
        
    def login(self):
        
        query = self.session.query(User).filter(User.email == self.__inputs.email).first()

        if validate_email_existance(query) != True:
            raise HTTPException(
                status_code=401,
                detail="Email or Password is incorrect!"
            )

        if validate_password(query, self.__inputs.password) != True:
            raise HTTPException(
                status_code=401,
                detail="Email or Password is incorrect!"
            )

        response = jsonable_encoder(
            {
                "full_names": query.full_names,
                "surname": query.surname,
                "email": query.email,
            }
        )

        return JSONResponse(
            status_code=201,
            content=response
        )
          