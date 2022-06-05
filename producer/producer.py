import json
import os
import time

from fake_data_generator import get_registered_user
from kafka import KafkaProducer
from kafka.errors import KafkaError
from loguru import logger

BROKER_HOST_NAME = os.environ.get("BROKER_HOST_NAME")
BROKER_HOST_PORT = os.environ.get("BROKER_HOST_PORT")


def json_serializer(data) -> json:
    """Serializing producers data to json."""
    return json.dumps(data).encode("utf-8")


def declare_producer() -> KafkaProducer | None:
    """Declare the Kafka producer."""
    try:
        _producer = KafkaProducer(
            bootstrap_servers=[BROKER_HOST_NAME + ":" + BROKER_HOST_PORT],
            value_serializer=json_serializer,
        )
    except KafkaError as _e:
        logger.debug(f"Broker Kafka is not available. Error: {_e}")
        _producer = None
    return _producer


if __name__ == "__main__":
    while True:
        logger.debug("Sending message to Kafka")
        registered_user = get_registered_user()
        producer = declare_producer()

        try:
            producer.send("registered_user", registered_user)
        except KafkaError as e:
            logger.debug(f"Broker Kafka is not available. Error: {e}")

        time.sleep(4)
