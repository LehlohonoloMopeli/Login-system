from sqlalchemy.orm import session
import logging
from app.database_model.user import User
from app.database_model import Session
from app.user_registration_service.model import UserRegistrationModel

#validators
from app.user_registration_service.validators.validate_email import validate_email_existance
from app.user_registration_service.validators.validate_password import validate_password_match
from pyisemail import is_email

#Responses
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class UserRegistration():
    
    def __init__(self, inputs: UserRegistrationModel):
        self.__inputs = inputs
        self.session = Session()
        
    def register_user(self):
        
        query = self.session.query(User).filter_by(email = self.__inputs.email).first()

        sql = User(
            full_names = self.__inputs.full_names,
            surname = self.__inputs.surname,
            id_number = self.__inputs.id_number,
            cell_number = self.__inputs.cell_number,
            email = self.__inputs.email,
            password = self.__inputs.password,
        )

        return self._extracted_from_register_user_15(query, sql)


    def _extracted_from_register_user_15(self, query, sql):
        if validate_email_existance(query) != True:
            raise HTTPException(
                status_code=401,
                detail="User already exists!"
            )

        if (
            validate_password_match(
                self.__inputs.password, self.__inputs.confirm_password
            )
            != True
        ):
            raise HTTPException(
                status_code=401,
                detail="Passwords do not match!"
            )
        if is_email(self.__inputs.email, check_dns=True) != True:
            raise HTTPException(
                status_code=401,
                detail="Invalid email address!"
            )
        self.session.add(sql)
        self.session.commit()
        response = {
            "status": "passed",
            "message": "You have successfully registered!"
        }
        return JSONResponse(
            status_code=201,
            content=response
        )
        