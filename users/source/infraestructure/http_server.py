from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from source.adapters.controllers.user import user_router
from source.infraestructure import models
from source.infraestructure import postgres

app = FastAPI()
models.Base.metadata.create_all(bind=postgres.engine)

app.include_router(user_router, prefix='/users')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4250", "http://localhost:4251"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

