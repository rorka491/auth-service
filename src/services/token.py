from typing import Optional
from jwt import decode, encode, InvalidTokenError
from datetime import timedelta, datetime
from src.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_LIFETIME_MINUTES, REFRESH_TOKEN_LIFETIME_DAYS
from src.exceptions.auth import InvalidTokenException
from src.core.logger import logger
from src.core.config import redis_client
import uuid



def create_access_token(user_id: int, expires_delta: timedelta = None) -> str:
    jti = str(uuid.uuid4())
    data = {"jti": jti, "sub": str(user_id), "type": "access"}
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=int(ACCESS_TOKEN_LIFETIME_MINUTES)))
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(user_id: int, expires_delta: timedelta = None) -> str:
    jti = str(uuid.uuid4())
    data = {"jti": jti, "sub": str(user_id), "type": "refresh"}
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=REFRESH_TOKEN_LIFETIME_DAYS))
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> Optional[dict]:
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return None
    
def verify_access_token(token: str)  -> Optional[dict]:
    payload = verify_token(token)
    logger.warning(payload)
    if not payload or payload.get("type") != "access":
        raise InvalidTokenException
    return payload
    
def verify_refresh_token(token: str) -> Optional[dict]:
    payload = verify_token(token)
    logger.warning(payload)
    if not payload or payload.get("type") != "refresh":
        raise InvalidTokenException
    return payload
    

# def extract_username_from_token(token: str) -> Optional[str]:
#     payload = verify_access_token(token)
#     if payload:
#         return payload.get("sub")
#     return None


def extract_user_id_from_token(token: str) -> Optional[str]:
    payload = verify_access_token(token)
    if payload:
        return payload.get("sub")
    return None


async def is_blacklisted(jti: str):
    return await redis_client.get(jti) is not None

async def blacklist_token(jti: str, exp_timestamp: int):
    ttl = exp_timestamp - int(datetime.utcnow().timestamp())
    await redis_client.set(jti, "revoked", ex=ttl)