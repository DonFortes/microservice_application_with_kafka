from db_config import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base

engine = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()
