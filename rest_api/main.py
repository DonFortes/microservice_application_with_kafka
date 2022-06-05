from database_queries import get_all_users_from_db, get_user_from_db_by_id
from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/")
async def index():
    text = "Microservice with Kafka. Path examples: 127.0.0.1:8000/api/v1/users or 127.0.0.1:8000/api/v1/user/1"
    return text


@app.get("/api/v1/users")
async def get_all_users():
    users = get_all_users_from_db()
    return users


@app.get("/api/v1/user/{user_id}")
async def get_user(user_id: int = Path(title="The id of the user to get")):
    user = get_user_from_db_by_id(user_id)
    return user
