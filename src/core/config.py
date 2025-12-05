from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from passlib.hash import argon2
from redis.asyncio import Redis

redis_client = Redis(host="localhost", port=6379, db=0)


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
SECRET_KEY = os.getenv("SECRET_KEY")
DB_NAME = os.getenv("DB_NAME")
HOST_ADRESS = os.getenv("HOST_ADRESS")
DB_TYPE = os.getenv('DB_TYPE')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_LIFETIME_MINUTES = int(os.getenv('ACCESS_TOKEN_LIFETIME_MINUTES'))
REFRESH_TOKEN_LIFETIME_DAYS = int(os.getenv('REFRESH_TOKEN_LIFETIME_DAYS'))

