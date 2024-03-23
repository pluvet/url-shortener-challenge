from fastapi import FastAPI
from source.adapters.controllers.user import user_router
from source.infraestructure.database import postgres, models

app = FastAPI()
models.Base.metadata.create_all(bind=postgres.engine)

app.include_router(user_router, prefix='/users')

