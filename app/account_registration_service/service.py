from app.database_model import Session
from .model import AccountregistrationModel
from app.database_model.bank_accounts import BankAccounts
from app.database_model.user import User

import datetime
from random import randint

#Responses
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class AccountRegistration:

    def __init__(self, inputs: AccountregistrationModel):
        self.session = Session()
        self.__inputs = inputs
        self.existing_accounts = self.query_accounts()
        self.account_number = self.create_account_number()

    def query_accounts(self):
        """
            Query existing account numbers.

        """
        return [
            account.account_number for account in self.session.query(BankAccounts)
        ]

    def create_random_numbers(self):
        """
            Return 11 random numbers

        """
        return randint(10000000000, 99999999999)


    def create_account_number(self):
        """
            Create new account number via a recursive function to ensure
            its uniqueness.

        """
        new_account_number = self.create_random_numbers()

        if new_account_number not in self.existing_accounts:
            return new_account_number
        else:
            self.create_account_number()

    def register_account(self):
        sql_user = User(
            # id_number = self.__inputs.id_number
        )

        sql_account = BankAccounts(
            account_number = self.account_number,
            account_type = self.__inputs.account_type,
            id_number = self.__inputs.id_number
        )

        sql_user.accounts.append(sql_account)

        self.session.add(sql_user)
        self.session.commit()
        self.session.close()

        response = {
            "message": "Congradulations! You have successfully registered a new account!",
            "new_account_number": f'{self.account_number}'
        }

        return JSONResponse(
            status_code=201,
            content=response
        )
