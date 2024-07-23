from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.UrlModel import Url


class UrlRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        original_url: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Url]:
        query = self.db.query(Url)

        if original_url:
            query = query.filter_by(original_url=original_url)

        return query.offset(start).limit(limit).all()

    def get(self, url: Url) -> Url:
        return self.db.get(
            Url,
            url.id,
        )

    def get_by_short_url(self, short_url: str) -> Optional[Url]:
        return self.db.query(Url).filter_by(short_url=short_url).first()

    def create(self, url: Url) -> Url:
        self.db.add(url)
        self.db.commit()
        self.db.refresh(url)
        return url

    def update(self, id: int, url: Url) -> Url:
        url.id = id
        self.db.merge(url)
        self.db.commit()
        return url

    def delete(self, url: Url) -> None:
        self.db.delete(url)
        self.db.commit()
        self.db.flush()