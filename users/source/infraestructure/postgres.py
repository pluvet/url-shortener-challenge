from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from source.infraestructure.env import pg_user, pg_password

URL_DATABASE = f'postgresql://{pg_user}:{pg_password}@pgdb:5432/user'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_gen = get_db()
db = next(db_gen)
