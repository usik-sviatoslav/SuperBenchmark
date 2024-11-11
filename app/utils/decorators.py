from functools import wraps

from fastapi import HTTPException

from app.core.config import settings


def debug_only(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not settings.DEBUG:
            raise HTTPException(status_code=503, detail="Feature not available in production mode")
        return await func(*args, **kwargs)

    return wrapper
