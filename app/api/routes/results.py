from datetime import datetime

from fastapi import APIRouter

from app.schemas.results import AverageResult
from app.services.results import calculate_average
from app.utils import debug_only, load_benchmarking_data

router = APIRouter()


@router.get("/average", response_model=AverageResult, status_code=200)
@debug_only
async def get_average_results():
    data = load_benchmarking_data()
    return calculate_average(data)


@router.get("/average/{start_time}/{end_time}", response_model=AverageResult, status_code=200)
@debug_only
async def get_average_results_by_time(start_time: datetime, end_time: datetime):
    data = load_benchmarking_data()
    filtered_data = [result for result in data if start_time <= result.timestamp <= end_time]

    return calculate_average(filtered_data)
