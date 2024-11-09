import uvicorn
from fastapi import FastAPI

from app.api.routers import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True, proxy_headers=True)
