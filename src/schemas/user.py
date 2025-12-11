from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from src.enums import UserRole

class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str = Field(min_length=6)
    org_id: Optional[int] = None


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: Optional[EmailStr]
    org_id: Optional[int]
    role: UserRole = UserRole.USER


class UserInDB(UserRead):
    hashed_password: str

class UserLogin(BaseModel):
    username: str 
    password: str


class UserList(BaseModel):
    users: list[UserRead]
