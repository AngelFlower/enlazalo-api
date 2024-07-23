from typing import Optional
from pydantic import BaseModel


class UrlPostRequestSchema(BaseModel):
    original_url: str
    expiration_date: Optional[str] = None
    password: Optional[str] = None


class UrlSchema(UrlPostRequestSchema):
    id: int
    short_url: str


class UrlResponseSchema(BaseModel):
    original_url: str
    short_url: str
    expiration_date: Optional[str] = None