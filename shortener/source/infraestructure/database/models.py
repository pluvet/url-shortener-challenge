from sqlalchemy import (
    Column,
    Integer,
    String
)

from source.infraestructure.database.postgres import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
