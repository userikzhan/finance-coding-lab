from fastapi import FastAPI

from app.routes.auth import router as auth_router

app = FastAPI(
    title="Finance Coding Lab"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Finance Coding Lab API"}
