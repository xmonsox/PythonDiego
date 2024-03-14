from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings



DB_URL = settings.DATABASE_URL
#CREAR UNA INSTANCIA DE MOTOR DE SQLALCHEMY
engine = create_engine(DB_URL)
# CREAR UNA INSTANCIA DE SESSIONMAKER
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# CREAR UNA CLASE BASE PARA LAS CLASES DE MODELO 
Base = declarative_base()
#FUNCION PARA CREAR LA SESION DE BASE DE DATOS
def get_session():
    session = SessionLocal()
    try: 
        yield session
    finally:
        session.close()