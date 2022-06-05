from create_database import engine
from loguru import logger
from models import User
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_all_users_from_db():
    """Get all users from User table"""
    with Session(engine) as session:
        logger.debug("Getting all users from database")
        statement = select(User).order_by(User.id)
        users = session.execute(statement)
        return users.scalars().all()


def get_user_from_db_by_id(user_id: int) -> User:
    """Get user by id from User table"""
    with Session(engine) as session:
        logger.debug("Getting user from database by id")
        user = session.query(User).get(user_id)
        return user
