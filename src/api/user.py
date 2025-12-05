from fastapi import APIRouter, Depends, Request
from src.services.user import UserService
from src.depends import get_user_service, get_current_user
from src.schemas.user import UserList, UserRead

router = APIRouter(prefix='/users')


@router.get("/list", response_model=list[UserRead])
async def all_users(
    user_service: UserService = Depends(get_user_service)
):
    users = await user_service.get_all()
    return users


@router.get('/me', response_model=UserRead)
async def me(
    requset: Request, 
    user_id: int = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    user = await user_service.get_user_by_id(id=user_id)
    return user
