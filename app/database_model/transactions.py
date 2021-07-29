from app.database_model import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, Integer, DateTime, Float
import datetime


class Transactions(Base):
    """
    Has a many-is-to-one relationship with bank_accounts table
    
    """

    __tablename__ = "transactions"

    transaction_id = Column(Integer(), primary_key=True, autoincrement=True)
    account_id = Column(Integer(), ForeignKey('bank_accounts.account_id'))
    created_on = Column(DateTime(), default=datetime.datetime.now)
    description = Column(String(50), nullable=False)
    transaction_type = Column(String(10), nullable=False)
    amount = Column(Float(), nullable=False)


    #Relationships
    account = relationship("BankAccounts", back_populates="transaction_details")
