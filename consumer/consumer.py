import json
import os

from create_database import create_db
from database_queries import insert_user_to_the_database
from kafka import KafkaConsumer
from loguru import logger

BROKER_HOST_NAME = os.environ.get("BROKER_HOST_NAME")
BROKER_HOST_PORT = os.environ.get("BROKER_HOST_PORT")


def declare_consumer() -> KafkaConsumer | None:
    """Declare Kafka Consumer to read messages from Kafka."""
    _consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers=[BROKER_HOST_NAME + ":" + BROKER_HOST_PORT],
        auto_offset_reset="earliest",
        group_id="registered_user_consumer_group",
    )
    return _consumer


if __name__ == "__main__":

    create_db()
    consumer = declare_consumer()

    for message in consumer:
        user = json.loads(message.value)
        try:
            insert_user_to_the_database(user)
        except Exception as e:
            logger.debug(f"An error occurred while inserting to database: {e}")
