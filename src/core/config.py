from pathlib import Path
from dotenv import load_dotenv
import os
from passlib.hash import argon2
from redis.asyncio import Redis


hasher = argon2.using(
    memory_cost=65536,
    time_cost=3,
    parallelism=4,
    salt_len=16,
    hash_len=32
)

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
HOST_ADRESS = os.getenv("HOST_ADRESS")
DB_TYPE = os.getenv('DB_TYPE')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_LIFETIME_MINUTES = int(os.getenv('ACCESS_TOKEN_LIFETIME_MINUTES'))
REFRESH_TOKEN_LIFETIME_DAYS = int(os.getenv('REFRESH_TOKEN_LIFETIME_DAYS'))
REDIS_HOST_ADRESS = os.getenv("REDIS_HOST_ADRESS")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_DB = int(os.getenv("REDIS_DB"))
PRIVATE_KEY = Path(os.getenv("PRIVATE_KEY_PATH")).read_text()
PUBLIC_KEY = Path(os.getenv("PUBLIC_KEY_PATH")).read_text()


redis_client = Redis(host=REDIS_HOST_ADRESS, port=REDIS_PORT, db=REDIS_DB)
