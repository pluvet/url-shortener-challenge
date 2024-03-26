from fastapi import FastAPI
from source.adapters.controllers.url import url_router
from source.infraestructure.database import postgres, models

app = FastAPI()
models.Base.metadata.create_all(bind=postgres.engine)

app.include_router(url_router, prefix='/urls')

