from fastapi import APIRouter, Response
from src.api.auth import router as auth_router
from src.api.user import router as user_router


router = APIRouter(prefix='/api/v1')
router.include_router(auth_router)
router.include_router(user_router)


@router.get('/ping')
async def ping():
    return {"status": "ok"}
