import pytest_asyncio
import pytest
from tortoise import Tortoise
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from asgi_lifespan import LifespanManager
from main import get_app

TEST_DB_URL = "sqlite://:memory:"   

@pytest_asyncio.fixture
async def client():
    test_app = get_app()
    await Tortoise.init(
        db_url=TEST_DB_URL,
        modules={"models": ["src.models"]}
    )
    await Tortoise.generate_schemas()

    transport = ASGITransport(app=test_app)
    async with LifespanManager(test_app):
        async with AsyncClient(transport=transport, base_url="http://testserver/api/v1") as ac:
            yield ac

    await Tortoise.close_connections()