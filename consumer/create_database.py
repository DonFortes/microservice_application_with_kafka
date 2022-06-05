from db_config import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base

engine = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()


def create_db() -> None:
    """Create tables in database."""
    DeclarativeBase.metadata.create_all(engine)
