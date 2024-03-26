from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl, Field
from source.application.create_shortened_url import CreateShortenedUrlService
from source.adapters.controllers.middleware import BearerTokenAuthBackend
from source.application.redirect_url import RedirectUrlService
from source.adapters.repositories.url.mongo import UrlMongoRepository


url_router = APIRouter()

class CreateUrlInputDTO(BaseModel):
    long_url: HttpUrl
    
class CreateUrlOutputDTO(BaseModel):
    short_url: str

@url_router.post('')
async def create(data: CreateUrlInputDTO, user_id = Depends(BearerTokenAuthBackend()))-> JSONResponse:
    """this function creates a new url"""

    url_repository = UrlMongoRepository()
    create_shortened_url_service = CreateShortenedUrlService(url_repository)

    short_url = await create_shortened_url_service.execute(
        user_id=user_id,
        long_url=data.long_url,
    )

    return CreateUrlOutputDTO(short_url=short_url)


class RedirectUrlOutputDTO(BaseModel):
    long_url: str

@url_router.get('/redirect/{key}')
async def redirect(key: int)-> JSONResponse:
    """this function redirects a short url"""

    url_repository = UrlMongoRepository()
    login_user_service = RedirectUrlService(url_repository)

    long_url = await login_user_service.execute(
        key=key
    )

    return RedirectUrlOutputDTO(long_url=long_url)
