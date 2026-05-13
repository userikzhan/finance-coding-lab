from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.get("/health")
def auth_health():
    return {"message": "Auth router works"}
