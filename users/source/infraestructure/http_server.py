from fastapi import FastAPI
from source.adapters.controllers.user import user_router
from source.infraestructure import models
from source.infraestructure import postgres

app = FastAPI()
models.Base.metadata.create_all(bind=postgres.engine)

app.include_router(user_router, prefix='/users')

