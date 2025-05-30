from typing import List, Optional

from fastapi import APIRouter, Depends, status

from schemas.pydantic.UrlSchema import (
   UrlResponseSchema,
#    UrlSchema,
   UrlPostRequestSchema
)
from services.UrlService import UrlService

UrlRouter = APIRouter(
    prefix="", tags=["url"]
)


# @UrlRouter.get("/", response_model=List[UrlSchema])
# def index(
#     original_url: Optional[str] = None,
#     pageSize: Optional[int] = 100,
#     startIndex: Optional[int] = 0,
#     urlService: UrlService = Depends(),
# ):
#     return [
#         url.normalize()
#         for url in urlService.list(
#             original_url, pageSize, startIndex
#         )
#     ]


# @UrlRouter.get("/{id}", response_model=UrlSchema)
# def get(id: int, urlService: UrlService = Depends()):
#     return urlService.get(id).normalize()

@UrlRouter.get(
    "/{short_url}",
    response_model=UrlResponseSchema,
)
def get_original_url(short_url: str, password: Optional[str] = None, urlService: UrlService = Depends()):
    return urlService.get_original_url(short_url=short_url, password=password).to_response()


@UrlRouter.post(
    "/",
    response_model=UrlResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    url: UrlPostRequestSchema,
    urlService: UrlService = Depends(),
):
    return urlService.create(url).to_response()


# @UrlRouter.patch("/{id}", response_model=UrlSchema)
# def update(
#     id: int,
#     url: UrlPostRequestSchema,
#     urlService: UrlService = Depends(),
# ):
#     return urlService.update(id, url).normalize()


# @UrlRouter.delete(
#     "/{id}", status_code=status.HTTP_204_NO_CONTENT
# )
# def delete(
#     id: int, urlService: UrlService = Depends()
# ):
#     return urlService.delete(id)


