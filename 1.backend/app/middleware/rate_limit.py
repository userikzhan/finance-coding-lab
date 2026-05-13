from fastapi import Request
from fastapi.responses import JSONResponse

request_count = {}


async def rate_limit_middleware(request: Request, call_next):

    client_ip = request.client.host

    request_count[client_ip] = request_count.get(client_ip, 0) + 1

    if request_count[client_ip] > 100:

        return JSONResponse(
            status_code=429,
            content={"detail": "Too many requests"}
        )

    response = await call_next(request)

    return response
