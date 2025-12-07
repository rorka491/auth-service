from os import access
from typing import Optional
from jose import jwt, JWTError
from datetime import timedelta, datetime, UTC
from src.core.config import PRIVATE_KEY, PUBLIC_KEY, ALGORITHM, ACCESS_TOKEN_LIFETIME_MINUTES, PUBLIC_KEY, REFRESH_TOKEN_LIFETIME_DAYS
from src.exceptions.auth import InvalidTokenException
from src.core.logger import logger
from src.core.config import redis_client
import uuid


def create_token(
    user_id: int, org_id: int, token_type: str, expires_delta: Optional[timedelta] = None
) -> str:
    """Создает JWT токен (access или refresh)"""
    expire = datetime.now(UTC) + (
        expires_delta or timedelta(minutes=int(ACCESS_TOKEN_LIFETIME_MINUTES))
        if token_type == "access"
        else timedelta(days=int(REFRESH_TOKEN_LIFETIME_DAYS))
    )

    payload = {
        "jti": str(uuid.uuid4()),
        "sub": str(user_id),
        "type": token_type,
        "exp": expire,
        "org_id": org_id
    }

    return jwt.encode(payload, PRIVATE_KEY, algorithm=ALGORITHM) # pyright: ignore[reportArgumentType]

def create_access_token(user_id: int, org_id, expires_delta: timedelta = None) -> str:
    access_token = create_token(
        user_id, org_id, expires_delta=expires_delta, token_type="access"
    )
    return access_token

def create_refresh_token(user_id: int, org_id, expires_delta: timedelta = None) -> str:
    refresh_token = create_token(
        user_id, org_id, expires_delta=expires_delta, token_type="refresh"
    )
    return refresh_token

def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(
            token, PUBLIC_KEY, algorithms=[ALGORITHM] # pyright: ignore[reportArgumentType]
        )
        return payload
    except JWTError:
        return None

def verify_access_token(token: str)  -> Optional[dict]:
    payload = verify_token(token)
    if not payload or payload.get("type") != "access":
        raise InvalidTokenException
    return payload

def verify_refresh_token(token: str) -> Optional[dict]:
    payload = verify_token(token)
    if not payload or payload.get("type") != "refresh":
        raise InvalidTokenException
    return payload

def extract_user_id_from_token(token: str) -> Optional[str]:
    payload = verify_access_token(token)
    if payload:
        return payload.get("sub")
    return None

async def is_blacklisted(jti: str):
    return await redis_client.get(jti) is not None

async def blacklist_token(jti: str, exp_timestamp: int):
    ttl = exp_timestamp - int(datetime.now(UTC).timestamp())
    await redis_client.set(jti, "revoked", ex=ttl)
