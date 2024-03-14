import datetime
from enum import Enum
from sqlalchemy import Column, String, Boolean, TIMESTAP, datetime
from sqlalchemy.orm import relationships
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User ():
    __tablename__ = 'users'
    
    user_id = Column(String(100), primary_key=true)
    full_name = Column(String(100))
    mail = Column(String(100), unique=True)
    passhash = Column(String(100))
    user_role = Column(String(100))
    user_status = Column(Boolean, default=True)
    created_at = Column(TIMESTAP, default=datetime.utcnow)
    updated_at = Column(DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow)

    transactions = relationships("Transaction", back_populates="user  ")