from abc import ABC, abstractmethod
from tortoise.models import Model
from tortoise.expressions import Q
from typing import Type, Optional, List, TypeVar
from src.models.user import User


M = TypeVar('M', bound=Model)

class AbstractRepository(ABC):
    model: Type[M]

    @abstractmethod
    async def get(self, **filters) -> Optional[M]:
        ...

    @abstractmethod
    async def get_all(self) -> List[M]:
        ...

    @abstractmethod
    async def filter(self, **filters) -> List[M]:
        ...

    @abstractmethod
    async def create(self, **data) -> M:
        ...

    @abstractmethod
    async def update(self, obj: M, **data) -> M:
        ...


class TortoiseRepository(AbstractRepository):
    
    async def get_all(self) :
        return await self.model.all()
    
    async def get(self, **filters):
        return await self.model.get_or_none(**filters)
    
    async def create(self, **data):
        return await self.model.create(**data)
    
    async def update(self, obj: M, **data):
        return await obj.update_from_dict(data)

    async def filter(self, **filters):
        return await self.model.filter(**filters)


class UserRepository(TortoiseRepository):
    model = User

    async def user_credentials_exists(self, username: str, email: str) -> bool:
        if not email:
            return await self.model.filter(username=username).exists()
        return await self.model.filter(Q(email=email) | Q(username=username)).exists()
    
    async def get_user_by_username(self, username: str) -> User | None:
        return await self.model.get_or_none(username=username)
