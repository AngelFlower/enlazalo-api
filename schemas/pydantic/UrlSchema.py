from pydantic import BaseModel


class UrlPostRequestSchema(BaseModel):
    original_url: str


class UrlSchema(UrlPostRequestSchema):
    id: int