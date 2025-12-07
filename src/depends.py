from jose import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from src.enums import UserRole
from src.models.user import User
from src.services.user import UserService
from src.services.auth import AuthService
from src.exceptions.auth import InvalidTokenException
from src.exceptions.admin import AdminsOnlyException
from src.core.config import SECRET_KEY, ALGORITHM
from src.services.token import verify_access_token

def get_user_service():
    return UserService()

def get_auth_service():
    return AuthService()

auth_scheme = HTTPBearer()


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)
) -> int:
    token = credentials.credentials
    payload = verify_access_token(token)
    user_id = payload.get("sub")
    
    if not user_id:
        raise InvalidTokenException

    return user_id


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    user_service: UserService = Depends(get_user_service)
) -> User:
    user_id = await get_current_user_id(credentials=credentials)
    user = await user_service.get_user_by_id(id=user_id)
    return user


async def get_current_admin(user=Depends(get_current_user)):
    if not user.role == UserRole.ADMIN:
        raise AdminsOnlyException
    return user
