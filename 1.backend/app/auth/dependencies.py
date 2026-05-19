from fastapi import HTTPException
from fastapi import Depends


async def require_admin(current_user=Depends(...)):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user
