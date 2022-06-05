from typing import Any

from faker import Faker

fake = Faker()


def get_registered_user() -> dict[str, Any]:
    """Create fake user's data to fill Kafka and database."""
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "year": fake.year(),
    }
    return user
