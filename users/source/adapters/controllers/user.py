from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from source.application.register_user import RegisterUserService
from source.application.login_user import LoginUserService
from source.adapters.repositories.user.postgres import PostgresUserRepository
from source.adapters.hash.password_encrypter import HashPasswordEncrypter
from source.adapters.jwt.token_generator import TokenGenerator
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
    password_encrypter = HashPasswordEncrypter()
    register_user_service = RegisterUserService(user_repository, password_encrypter)

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
    password_encrypter = HashPasswordEncrypter()
    token_generator = TokenGenerator()
    login_user_service = LoginUserService(user_repository, password_encrypter, token_generator)

    try:
        token = await login_user_service.execute(
            email=data.email,
            password=data.password,
        )
    except InvalidEmailOrPassword:
        raise HTTPException(404, detail="Incorrect Email or Password")

    return LoginUserOutputDTO(token=token)
