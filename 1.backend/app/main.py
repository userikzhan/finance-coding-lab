from fastapi import FastAPI

from app.api.routes import router as api_router
from app.auth import router as auth_router

app = FastAPI(
    title="Finance AI OS"
)

app.include_router(api_router)

app.include_router(auth_router)
