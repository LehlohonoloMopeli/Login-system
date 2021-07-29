from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, DateTime, Float

from app.database_model import Base
import datetime


class BankAccounts(Base):
    """
    Has a many-is-to-one relationship with user table

    Has a one-is-to-many relatioship with transactions table 
    
    """

    __tablename__ = "bank_accounts"

    account_id = Column(Integer(), primary_key=True, autoincrement=True)
    id_number = Column(String(13), ForeignKey('user.id_number'))
    created_on = Column(DateTime(), default=datetime.datetime.now)
    account_number = Column(Integer(), nullable=False, unique=True)
    account_type = Column(String(10), nullable=False)
    balance = Column(Float(), nullable=False, default=0.00)
    last_updated = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)


    #Relationships
    user_details = relationship("User", back_populates="accounts")
    transaction_details = relationship("Transactions", back_populates="account")
