from fastapi import APIRouter, Depends

from app.auth.dependencies import require_admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# =====================================================
# Admin panel endpoint
#
# Доступ:
# только admin users
# =====================================================

@router.get("/")
async def admin_panel(

    # Проверка admin доступа
    current_user=Depends(require_admin)

):

    return {
        "status": "ok",
        "message": "Welcome admin"
    }
