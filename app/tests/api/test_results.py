import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app
from app.schemas import AverageResult

client = TestClient(app)


@pytest.mark.parametrize("debug_mode", (True, False))
def test_get_average_results(mocker, debug_mode):
    # Mock DEBUG setting
    mocker.patch.object(settings, "DEBUG", debug_mode)

    # Get response
    response = client.get("/results/average")
    response_data = response.json()

    if debug_mode:  # Check that returns correct response data in DEBUG mode
        assert response.status_code == 200
        assert AverageResult(**response_data)

    else:  # Check that feature not realized
        assert response.status_code == 503
        assert response_data == {"detail": "Feature not ready for live yet"}


@pytest.mark.parametrize("debug_mode", (True, False))
def test_get_average_results_by_time(mocker, debug_mode):
    # Mock DEBUG setting
    mocker.patch.object(settings, "DEBUG", debug_mode)

    start_time = "2024-06-01T12:00:00"
    end_time = "2024-06-02T11:00:00"

    # Get response
    response = client.get(f"/results/average/{start_time}/{end_time}")
    response_data = response.json()

    if debug_mode:  # Check that returns correct response data in DEBUG mode
        assert response.status_code == 200
        assert AverageResult(**response_data)

    else:  # Check that feature not realized
        assert response.status_code == 503
        assert response_data == {"detail": "Feature not ready for live yet"}
