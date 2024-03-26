from sqlalchemy import (
    Column,
    Integer,
    String
)

from source.infraestructure.database.postgres import Base

class Url(Base):
    __tablename__ = "urls"
    
    key = Column(String(6), primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    long_url = Column(String(255), nullable=False)
    visits = Column(Integer)
