from fastapi import Request
from fastapi.responses import JSONResponse


async def auth_middleware(request: Request, call_next):

    response = await call_next(request)

    return response
