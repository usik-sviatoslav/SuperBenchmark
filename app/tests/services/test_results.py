from datetime import datetime

from app.schemas import AverageResult, BenchmarkingResult
from app.services.results import calculate_average


def benchmark_spec(
    token_count: int, time_to_first_token: int, time_per_output_token: int, total_generation_time: int
) -> BenchmarkingResult:
    return BenchmarkingResult(
        request_id="1",
        prompt_text="Translate the following English text to French: 'Hello, how are you?'",
        generated_text="Bonjour, comment ça va?",
        token_count=token_count,
        time_to_first_token=time_to_first_token,
        time_per_output_token=time_per_output_token,
        total_generation_time=total_generation_time,
        timestamp=datetime.fromisoformat("2024-06-01T12:00:00"),
    )


def test_calculate_average():
    data = [
        benchmark_spec(10, 100, 20, 300),
        benchmark_spec(20, 200, 30, 800),
        benchmark_spec(30, 300, 40, 1500),
    ]

    result = calculate_average(data)

    expected_average = AverageResult(
        average_token_count=(10 + 20 + 30) / 3,
        average_time_to_first_token=(100 + 200 + 300) / 3,
        average_time_per_output_token=(20 + 30 + 40) / 3,
        average_total_generation_time=(300 + 800 + 1500) / 3,
    )

    assert result == expected_average
