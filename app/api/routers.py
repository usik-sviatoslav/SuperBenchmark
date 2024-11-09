from fastapi import APIRouter

from .routes import results_router

api_router = APIRouter()

api_router.include_router(results_router, prefix="/results", tags=["Benchmark Results"])
