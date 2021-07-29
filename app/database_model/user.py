from app.database_model import Base
from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.orm import relationship, backref
import datetime

class User(Base):
    """
    Has a one-is-to-many relationship with bank_accounts table

    """
    
    __tablename__ = "user"
    
    full_names = Column(String(40), nullable=False)
    surname = Column(String(20), nullable=False)
    id_number = Column(String(13), nullable=False, primary_key=True)
    cell_number = Column(String(12), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    last_updated = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)


    #Relationships
    accounts = relationship("BankAccounts", back_populates="user_details")
