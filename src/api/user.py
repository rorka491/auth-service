from fastapi import APIRouter, Depends, Request
from src.services.user import UserService
from src.depends import get_user_service, get_current_user_id, get_current_admin
from src.schemas.user import UserList, UserRead
from src.models.user import User

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/list", response_model=list[UserRead])
async def all_users(
    admin: User = Depends(get_current_admin),
    user_service: UserService = Depends(get_user_service)
):
    users = await user_service.get_all()
    return users


@router.get('/me', response_model=UserRead)
async def me(
    requset: Request, 
    user_id: int = Depends(get_current_user_id),
    user_service: UserService = Depends(get_user_service)
):
    user = await user_service.get_user_by_id(id=user_id)
    return user
