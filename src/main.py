from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .users.router import router as users_router
from .auth.router import router as auth_router
from .constants import ALLOWED_ORIGIN
from .exceptions import (
    not_authenticated_exception_handler,
    NotAuthenticatedException,
)

exception_handlers = {
    NotAuthenticatedException: not_authenticated_exception_handler
}

app = FastAPI(exception_handlers=exception_handlers)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(auth_router)
