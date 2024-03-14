from datetime import datetime
from sqlalchemy import Column, String, Boolean, TIMESTAMP, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
# from db.session import Base

class User():
    __tablename__ = 'users'
    # __table_args__ = {'schema': 'public'}  # Especifica el esquema de la tabla

    user_id = Column(String(100), primary_key=True)
    full_name = Column(String(100))
    mail = Column(String(100), unique=True)
    passhash = Column(String(100))
    user_role = Column(String(100))
    user_status = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    transactions = relationship("Transaction", back_populates="user")
