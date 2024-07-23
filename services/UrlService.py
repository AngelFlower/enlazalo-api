import string
import secrets
import datetime

from typing import List, Optional

from fastapi import Depends, HTTPException
from models.UrlModel import Url

from repositories.UrlRepository import UrlRepository
from utils.password import hash_password, verify_password


class UrlService:
    urlRepository: UrlRepository

    def __init__(
        self, urlRepository: UrlRepository = Depends()
    ) -> None:
        self.urlRepository = urlRepository

    def _generate_unique_short_url(self) -> str:
        while True:
            short_url = generate_short_url()
            if not self.urlRepository.get_by_short_url(short_url):
                return short_url

    def create(self, url_body: Url) -> Url:
        short_url = self._generate_unique_short_url()
        password = hash_password(url_body.password) if url_body.password is not None else None
        new_url = Url(original_url=url_body.original_url, short_url=short_url, 
                      expiration_date= url_body.expiration_date, password=password)
        return self.urlRepository.create(new_url)

    def delete(self, url_id: int) -> str:
        url_instance = self.urlRepository.get(Url(id=url_id)) # Get instance
        if url_instance:
            self.urlRepository.delete(url_instance)
            return "Url deleted successfully"
        else:
            raise ValueError(f"Url with id {url_id} not found")

    def get(self, url_id: int) -> Url:
        return self.urlRepository.get(
            Url(id=url_id)
        )
    
    def get_original_url(self, short_url: str, password: Optional[str] = None) -> Url:
        url = self.urlRepository.get_by_short_url(short_url=short_url)
        if url is None:
            raise HTTPException(status_code=404, detail="URL not found")
        
        if url.expiration_date and url.expiration_date <= datetime.datetime.now():
            raise HTTPException(status_code=403, detail="This URL has expired")

        if url.password:
            if not password:
                raise HTTPException(status_code=403, detail="This URL requires a password to access.")
            same_pass = verify_password(hashed_password=url.password, input_password=password)
            if not same_pass:
                raise HTTPException(status_code=403, detail="Incorrect password.")
        return url

    def list(
        self,
        original_url: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Url]:
        return self.urlRepository.list(
            original_url, pageSize, startIndex
        )

    def update(
        self, url_id: int, url_body: Url
    ) -> Url:
        return self.urlRepository.update(
            url_id, Url(original_url=url_body.original_url)
        )



def generate_short_url(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    short_url = ''.join(secrets.choice(characters) for _ in range(length))
    return short_url
