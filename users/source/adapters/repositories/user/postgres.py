from dataclasses import dataclass
from source.domain.user import User
from source.infraestructure.postgres import db
from source.infraestructure import models
from sqlalchemy import exc

@dataclass
class PostgresUserRepository:

    async def save(self, user: User) -> int:
        new_user = models.User(**user.model_dump())
        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except exc.IntegrityError:
            db.flush()
            db.rollback()
        return new_user.id
    
    async def find_by_email(self, email: str) -> User:

        user = db.query(models.User).filter(models.User.email == email).first()
        return User(
            id=user.id,
            email=user.email,
            password=user.password
        )
