from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str = Field(min_length=6)


class UserRead(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr]

    class Config:
        from_attributes = True


class UserInDB(UserRead):
    hashed_password: str

class UserLogin(BaseModel):
    username: str 
    password: str


class UserList(BaseModel):
    users: list[UserRead]

