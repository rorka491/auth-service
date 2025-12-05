from fastapi import HTTPException, status




InvalidUserCredentials = HTTPException(status_code=401, detail="Invalid credentials")
InvalidTokenException = HTTPException(status_code=401, detail="Invalid token")
TokenBlackListedException = HTTPException(status_code=401, detail="Refresh token is blacklisted")
JtiNotProvided = HTTPException(status_code=401, detail="Jti not excpired")