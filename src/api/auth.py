from fastapi import APIRouter, Request, Response, Depends, Body
from src.schemas.user import UserCreate, UserRead, UserLogin
from src.schemas.token import TokenResponse, RefreshTokenRequest
from src.depends import get_user_service, get_auth_service
from src.services.user import UserService
from src.services.auth import AuthService
from src.core.logger import logger


router = APIRouter(prefix='/auth')


@router.post('/register', response_model=UserRead)
async def register(
    request: Request, 
    data: UserCreate, 
    user_service: UserService = Depends(get_user_service)
):
    user = await user_service.create_user(data)
    return user


@router.post('/login', response_model=TokenResponse)
async def login(
    request: Request,
    data: UserLogin,
    auth_service: AuthService = Depends(get_auth_service)
):
    access_token, refresh_token = await auth_service.authenticate_user(data)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post('/refresh', response_model=TokenResponse)
async def refresh(
    request: Request,
    data: RefreshTokenRequest,
    auth_service: AuthService = Depends(get_auth_service)
):
    access_token = await auth_service.get_new_access_token(data.refresh_token)
    return TokenResponse(access_token=access_token)


@router.post('/logout')
async def logout(
    data: RefreshTokenRequest,
    auth_service: AuthService = Depends(get_auth_service)
):
    await auth_service.logout(data.refresh_token)
    return {"detail": "Logged out successfully"}