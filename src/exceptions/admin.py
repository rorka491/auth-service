from fastapi import HTTPException, status


AdminsOnlyException = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admins only")
