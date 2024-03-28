from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, AnyUrl, Field
from source.domain.url import Url
from source.application.create_shortened_url import CreateShortenedUrlService
from source.application.get_all_url import GetAllUrlService
from source.adapters.controllers.middleware import BearerTokenAuthBackend
from source.application.redirect_url import RedirectUrlService
from source.adapters.repositories.url.mongo import UrlMongoRepository
from source.infraestructure.env import short_url


url_router = APIRouter()

class CreateUrlInputDTO(BaseModel):
    long_url: AnyUrl
    
class CreateUrlOutputDTO(BaseModel):
    short_url: str

@url_router.post('')
async def create(data: CreateUrlInputDTO, user_id = Depends(BearerTokenAuthBackend()))-> JSONResponse:
    """this function creates a new url"""

    url_repository = UrlMongoRepository()
    create_shortened_url_service = CreateShortenedUrlService(url_repository)

    url = await create_shortened_url_service.execute(
        user_id=user_id,
        long_url=str(data.long_url),
        short_url=short_url
    )

    return CreateUrlOutputDTO(short_url=url)

class GetAllUrlOutputDTO(BaseModel):
    urls: list[Url]

@url_router.get('')
async def list(user_id = Depends(BearerTokenAuthBackend()))-> JSONResponse:
    """this function lists all url"""

    url_repository = UrlMongoRepository()
    get_all_url_service = GetAllUrlService(url_repository)

    urls = await get_all_url_service.execute(
        user_id=user_id
    )

    return GetAllUrlOutputDTO(urls=urls)

class RedirectUrlOutputDTO(BaseModel):
    long_url: str

@url_router.get('/redirect/{key}')
async def redirect(key: str)-> JSONResponse:
    """this function redirects a short url"""

    url_repository = UrlMongoRepository()
    login_user_service = RedirectUrlService(url_repository)

    long_url = await login_user_service.execute(
        key=key
    )

    return RedirectUrlOutputDTO(long_url=long_url)
