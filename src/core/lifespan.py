from fastapi import FastAPI
from contextlib import asynccontextmanager
from passlib.hash import bcrypt
from src.models import User
from tortoise.exceptions import DoesNotExist
import os
from src.core.config import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_USERNAME
from src.core.config import hasher 
from src.enums import UserRole


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        await User.get(username=ADMIN_USERNAME)
    except DoesNotExist:
        await User.create(
            username=ADMIN_USERNAME,
            email=ADMIN_EMAIL,
            password=hasher.hash(ADMIN_PASSWORD),
            role=UserRole.ADMIN.value
        )
        print("Admin created")
    
    yield  