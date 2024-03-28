from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from source.adapters.controllers.url import url_router
from source.infraestructure.database import postgres, models

app = FastAPI()
models.Base.metadata.create_all(bind=postgres.engine)

app.include_router(url_router, prefix='/urls')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4250", "http://localhost:4251"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

