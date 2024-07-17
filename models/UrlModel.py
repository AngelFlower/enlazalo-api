from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta


class Url(EntityMeta):
    __tablename__ = "urls"

    id = Column(Integer)
    original_url = Column(String(200), nullable=False)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "original_url": self.original_url.__str__(),
        }