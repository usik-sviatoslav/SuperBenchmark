from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.schemas.results import AverageResult
from app.services.results import calculate_average
from app.utils.json_handler import load_benchmarking_data

router = APIRouter()


@router.get("/average", response_model=AverageResult, status_code=200)
async def get_average_results():
    if not settings.DEBUG:
        raise HTTPException(status_code=503, detail="Feature not ready for live yet")

    data = load_benchmarking_data()
    return calculate_average(data)


@router.get("/average/{start_time}/{end_time}", response_model=AverageResult, status_code=200)
async def get_average_results_by_time(start_time: datetime, end_time: datetime):
    if not settings.DEBUG:
        raise HTTPException(status_code=503, detail="Feature not ready for live yet")

    data = load_benchmarking_data()
    filtered_data = [result for result in data if start_time <= result.timestamp <= end_time]

    return calculate_average(filtered_data)
