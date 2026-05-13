from fastapi import Request

from app.middleware.logger import logger


async def logging_middleware(request: Request, call_next):

    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    return response
