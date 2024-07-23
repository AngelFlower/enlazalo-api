from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    TIMESTAMP
)

from models.BaseModel import EntityMeta


class Url(EntityMeta):
    __tablename__ = "urls"

    id = Column(Integer)
    original_url = Column(String(200), nullable=False)
    short_url = Column(String(50), unique=True, index=True, nullable=False)
    expiration_date = Column(TIMESTAMP, nullable=True)
    password = Column(String, nullable=True)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "original_url": self.original_url.__str__(),
            "short_url": self.short_url.__str__(),
            "expiration_date": self.expiration_date.__str__(),
            "password": self.password.__str__()
        }
    
    def to_response(self):
        return {
            "original_url": self.original_url.__str__(),
            "short_url": self.short_url.__str__(),
            "expiration_date": self.expiration_date.__str__(),
        }