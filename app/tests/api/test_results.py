import pytest

from app.schemas import AverageResult


@pytest.mark.usefixtures("disable_debug_only")
@pytest.mark.asyncio
class TestResults:
    async def test_get_average_results(self, async_client):
        # Get response
        response = await async_client.get("/results/average")
        response_data = response.json()

        # Check that returns correct response data
        assert response.status_code == 200
        assert AverageResult(**response_data)

    async def test_get_average_results_by_time(self, async_client):
        start_time = "2024-06-01T12:00:00"
        end_time = "2024-06-02T11:00:00"

        # Get response
        response = await async_client.get(f"/results/average/{start_time}/{end_time}")
        response_data = response.json()

        # Check that returns correct response data
        assert response.status_code == 200
        assert AverageResult(**response_data)
