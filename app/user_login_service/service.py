from app.database_model import Session
from app.database_model.user import User
from app.user_login_service.validators.validate_user import validate_email_existance
from app.user_login_service.validators.validate_user import validate_password
from .model import LoginModel

class Login():
    
    def __init__(self, inputs: LoginModel):
        self.__inputs = inputs
        self.session = Session()
        
    def login(self):
        
        query = self.session.query(User).filter_by(email = self.__inputs.email).first()

        if validate_email_existance(query) != True:
            return {
                "status": "failed",
                "message": "Email or Password is incorrect!"
            }
        if validate_password(query, self.__inputs.password) == True:

            return {
                "full_names": query.full_names,
                "surname": query.surname,
                "email": self.__inputs.email
            }

        else:
            return {
                "status": "failed",
                "message": "Email or Password is incorrect!"
            }