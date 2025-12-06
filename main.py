from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.router import router
from src.core.db import TORTOISE_ORM
# from src.core.lifespan import lifespan
from src.core.logger import logger

def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app

app = FastAPI()
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
)

app.include_router(router)