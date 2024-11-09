import json
from pathlib import Path
from typing import List

from app.schemas import BenchmarkingResult


def load_benchmarking_data() -> List[BenchmarkingResult]:
    app_dir = Path(__file__).resolve().parent.parent
    file_path = app_dir / "tests" / "test_database.json"

    with open(file_path, "r") as file:
        data = json.load(file)["benchmarking_results"]

    return [BenchmarkingResult(**item) for item in data]
