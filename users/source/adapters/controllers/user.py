from fastapi import APIRouter, HTTPException
import jwt
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from source.application.register_user import RegisterUserService
from source.application.login_user import LoginUserService
from source.adapters.repositories.user.postgres import PostgresUserRepository
from source.application.exceptions import InvalidEmailOrPassword

user_router = APIRouter()

class RegisterUserInputDTO (BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)
    
class RegisterUserOutputDTO (BaseModel):
    id: int

@user_router.post('/register')
async def register(data: RegisterUserInputDTO)-> JSONResponse:
    """this function register a new user"""

    user_repository = PostgresUserRepository()
    register_user_service = RegisterUserService(user_repository)

    id = await register_user_service.execute(
        email=data.email,
        password=data.password,
    )

    return RegisterUserOutputDTO(id=id)

class LoginUserInputDTO (BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)

class LoginUserOutputDTO (BaseModel):
    token: str

@user_router.post('/login')
async def login(data: LoginUserInputDTO)-> JSONResponse:
    """this function login"""

    user_repository = PostgresUserRepository()
    login_user_service = LoginUserService(user_repository)

    try:
        token = await login_user_service.execute(
            email=data.email,
            password=data.password,
        )
    except InvalidEmailOrPassword:
        raise HTTPException(404, detail="Incorrect Email or Password")

    return LoginUserOutputDTO(token=token)
