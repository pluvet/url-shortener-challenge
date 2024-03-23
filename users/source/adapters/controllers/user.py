from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from source.services.register_user import RegisterUserService
from source.services.login_user import LoginUserService
from source.adapters.repositories.user.postgres import PostgresUserRepository

user_router = APIRouter()

@user_router.post('/register')
async def register(request: Request)-> JSONResponse:
    """this function register a new user"""
    request = await request.json()

    user_repository = PostgresUserRepository()
    register_user_service = RegisterUserService(user_repository)

    user_id = await register_user_service.execute(
        email=request["email"],
        password=request["password"],
    )

    return JSONResponse({"user_id": user_id}, status_code=201)

@user_router.post('/login')
async def login(request: Request)-> JSONResponse:
    """this function login"""
    request = await request.json()

    user_repository = PostgresUserRepository()
    login_user_service = LoginUserService(user_repository)

    token = await login_user_service.execute(
        email=request["email"],
        password=request["password"],
    )

    return JSONResponse({"token": token}, status_code=200)

