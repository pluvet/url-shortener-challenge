from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, AnyUrl
from source.domain.url import Url
from source.application.create_shortened_url import CreateShortenedUrlService
from source.application.get_all_url import GetAllUrlService
from source.adapters.controllers.middleware import BearerTokenAuthBackend
from source.application.redirect_url import RedirectUrlService
from source.adapters.repositories.url.mongo import UrlMongoRepository
from source.adapters.key.generator import ShortUUIDGenerator
from source.infraestructure.env import base_url
from source.application.exceptions import NotFound, MaximumCollisionRetriesReached

url_router = APIRouter()

class CreateUrlInputDTO(BaseModel):
    long_url: AnyUrl
    
class CreateUrlOutputDTO(BaseModel):
    short_url: str

@url_router.post('', status_code=201)
async def create(data: CreateUrlInputDTO, user_id = Depends(BearerTokenAuthBackend()))-> JSONResponse:
    """this function creates a new url"""

    url_repository = UrlMongoRepository()
    key_generator = ShortUUIDGenerator()
    create_shortened_url_service = CreateShortenedUrlService(url_repository, key_generator)

    try:
        url = await create_shortened_url_service.execute(
            user_id=user_id,
            long_url=str(data.long_url),
            base_url=base_url
        )
    except MaximumCollisionRetriesReached:
        raise HTTPException(500, detail="Key Collision")

    return CreateUrlOutputDTO(short_url=url)

class GetAllUrlOutputDTO(BaseModel):
    urls: list[Url]

@url_router.get('', status_code=200)
async def list(user_id = Depends(BearerTokenAuthBackend()))-> JSONResponse:
    """this function lists all url that belongs to one user"""

    url_repository = UrlMongoRepository()
    get_all_url_service = GetAllUrlService(url_repository)

    urls = await get_all_url_service.execute(
        user_id=user_id
    )

    return GetAllUrlOutputDTO(urls=urls)

class RedirectUrlOutputDTO(BaseModel):
    long_url: str

@url_router.get('/redirect/{key}', status_code=200)
async def redirect(key: str)-> JSONResponse:
    """this function receive the key of a short url and returns a long url"""

    url_repository = UrlMongoRepository()
    redirect_service = RedirectUrlService(url_repository)

    try:
        long_url = await redirect_service.execute(
            key=key
        )
    except NotFound:
        raise HTTPException(404, detail="Url not found")

    return RedirectUrlOutputDTO(long_url=long_url)
