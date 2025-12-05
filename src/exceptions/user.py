from fastapi import HTTPException, status



UserAlreadyExistsException = HTTPException(status_code=400, detail="User already exists")
UserNotFoundNotAuthException = HTTPException(status_code=401, detail="User not found")


