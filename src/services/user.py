from typing import TYPE_CHECKING
from tortoise.expressions import Q
from src.repo import UserRepository
from src.schemas.user import UserCreate
from src.exceptions.user import UserAlreadyExistsException, UserNotFoundNotAuthException
from src.models.user import User
from src.core.config import hasher

class UserService: 
    def __init__(self):
        self.hasher = hasher
        self.repo = UserRepository()

    async def get_all(self) -> list[User]:
        return await self.repo.get_all()

    async def create_user(self, data: UserCreate):
        exists = await self.repo.user_credentials_exists(
            username=data.username,
            email=data.email
        )
        if exists:
            raise UserAlreadyExistsException
        
        password = data.password
        hash_password = self.hasher.hash(password)
        data.password = hash_password
        return await self.repo.create(**data.model_dump())
    
    
    async def get_user_by_username(self, username):
        user = await self.repo.get_user_by_username(username)
        if not user:
            raise UserNotFoundNotAuthException
        return user
    
    async def get_user_by_id(self, id: int) -> User:
        user = await self.repo.get(id=id)
        if not user:
            raise UserNotFoundNotAuthException
        return user


