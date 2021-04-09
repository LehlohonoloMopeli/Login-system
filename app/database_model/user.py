from . import Base
from sqlalchemy import Column, String, Integer, DateTime, Date
import datetime

class User(Base):
    __tablename__ = "user"
    
    user_id = Column(Integer(), autoincrement=True, primary_key=True)
    
    full_names = Column(String(40), nullable=False)
    surname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    last_updated = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)