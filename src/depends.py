import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from src.services.user import UserService
from src.services.auth import AuthService
from src.exceptions.auth import InvalidTokenException
from src.core.config import SECRET_KEY, ALGORITHM

def get_user_service():
    return UserService()

def get_auth_service():
    return AuthService()

auth_scheme = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise InvalidTokenException
    
    user_id = payload.get("sub")
    if not user_id:
        raise InvalidTokenException
    
    return user_id
