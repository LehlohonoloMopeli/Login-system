from sqlalchemy.orm import session
import logging
from app.database_model.user import User
from app.database_model import Session
from app.user_registration_service.model import UserRegistrationModel
from app.user_registration_service.validators.validate_email import validate_email_existance
from app.user_registration_service.validators.validate_password import validate_password_match
from app.user_registration_service.validators.validate_email import validate_email_format

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
        
        try:
            if validate_email_existance(query) == True:
                if validate_password_match(self.__inputs.password, self.__inputs.confirm_password) == True:
                    if validate_email_format(self.__inputs.email) == True:
                        
                        self.session.add(sql)
                        self.session.commit()
                        return {
                            "status": "passed",
                            "message": "You have successfully registered!"
                        }
                    else:
                        return {
                            "status": "failed",
                            "message": "Invalid email address!"
                        }
                else:
                    return {
                        "status": "failed",
                        "message": "Passwords do not match!"
                    }
            else:
                return {
                    "status": "failed",
                    "message": "User already exists!"
                }
                
        except Exception as error:
            logging.error("User Registration: " + str(error))
            return str(error)
        