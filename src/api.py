from fastapi import APIRouter

from src.auth.router import router as auth_router


api_router = APIRouter(prefix="/api")

api_router.include_router(auth_router)
