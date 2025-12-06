import pytest
from httpx import AsyncClient
from tests.conf_test import client

@pytest.mark.asyncio
async def test_auth_flow(client: AsyncClient):
    username = "testuser"
    password = "Password123!"

    response = await client.post('/auth/register', json={"username": username, "password": password})
    assert response.status_code == 200

    response = await client.post("/auth/login", json={"username": username, "password": password})
    assert response.status_code == 200
    data = response.json()
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    assert access_token
    assert refresh_token

    response = await client.get("/users/me", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200

    response = await client.post("/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    new_access_token = response.json()["access_token"]
    assert new_access_token != access_token

    response = await client.post("/auth/logout", json={"refresh_token": refresh_token})
    assert response.status_code == 200

    response = await client.post("/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 401 

