from create_database import DeclarativeBase
from sqlalchemy import Column, Integer, String


class User(DeclarativeBase):

    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    year = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"
