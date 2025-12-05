from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class AccessTokenRequest(BaseModel):
    access_token: str