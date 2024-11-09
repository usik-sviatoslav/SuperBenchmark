from typing import List

from app.schemas import AverageResult, BenchmarkingResult


def calculate_average(results: List[BenchmarkingResult]) -> AverageResult:
    total_token_count = sum(r.token_count for r in results)
    total_time_to_first_token = sum(r.time_to_first_token for r in results)
    total_time_per_output_token = sum(r.time_per_output_token for r in results)
    total_generation_time = sum(r.total_generation_time for r in results)
    count = len(results)

    return AverageResult(
        average_token_count=total_token_count / count,
        average_time_to_first_token=total_time_to_first_token / count,
        average_time_per_output_token=total_time_per_output_token / count,
        average_total_generation_time=total_generation_time / count,
    )
