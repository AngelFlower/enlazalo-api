from typing import List, Optional

from fastapi import Depends
from models.UrlModel import Url

from repositories.UrlRepository import UrlRepository
from schemas.pydantic.UrlSchema import UrlSchema


class UrlService:
    urlRepository: UrlRepository

    def __init__(
        self, urlRepository: UrlRepository = Depends()
    ) -> None:
        self.urlRepository = urlRepository

    def create(self, url_body: Url) -> Url:
        return self.urlRepository.create(
            Url(original_url=url_body.original_url)
        )

    def delete(self, url_id: int) -> str:
        url_instance = self.urlRepository.get(Url(id=url_id))  # Obtener la instancia primero
        if url_instance:
            self.urlRepository.delete(url_instance)
            return "Url deleted successfully"
        else:
            raise ValueError(f"Url with id {url_id} not found")

        # return self.urlRepository.delete(
        #     Url(id=url_id)
        # )

    def get(self, url_id: int) -> Url:
        return self.urlRepository.get(
            Url(id=url_id)
        )

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
