# from fastapi import FastAPI
# from contextlib import asynccontextmanager
# from fastapi_admin.providers.login import UsernamePasswordProvider
# from src.core.db import TORTOISE_ORM
# from src.admin.admin_app import admin_app
# from src.core.logger import logger
# from redis.asyncio import Redis
# from src.models.admin import Admin as AdminModel

# redis = Redis(host="localhost", port=6379, db=0)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await admin_app.configure(
#         redis=redis,
#         providers=[
#             UsernamePasswordProvider(
#                 admin_model=AdminModel,
#             )
#         ],
#     )
#     logger.info('Admin app init')
#     yield
#     await redis.close()

