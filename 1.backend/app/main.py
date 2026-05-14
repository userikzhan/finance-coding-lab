from fastapi import FastAPI

from app.api.routes import router as api_router
from app.routes.auth import router as auth_router
from app.routes.upload import router as upload_router

app = FastAPI(
    title="Finance Coding Lab"
)

# API routes
app.include_router(api_router)

# Auth routes
app.include_router(auth_router)

# Upload routes
app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Finance Coding Lab API"
    }
