from create_database import engine
from loguru import logger
from models import User
from sqlalchemy.orm import Session


def insert_user_to_the_database(user) -> None:
    """Fill database with fake User data. Function to commit changes in database."""
    with Session(engine) as session:
        instance = User(
            name=user["name"],
            address=user["address"],
            year=int(user["year"]),
        )
        session.add(instance)
        session.commit()
        logger.debug("User has been successfully inserted to database.")
