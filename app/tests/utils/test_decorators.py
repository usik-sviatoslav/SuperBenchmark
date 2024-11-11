import pytest
from fastapi import HTTPException

from app.core.config import settings
from app.utils import debug_only


@debug_only
async def some_function():
    """Test function to which the decorator is applied"""
    return "Function successfully executed!"


@pytest.mark.asyncio
async def test_debug_only_decorator_debug_enabled(mocker):
    # Mock the DEBUG setting as True
    mocker.patch.object(settings, "DEBUG", True)

    # Check that the function is executed successfully
    result = await some_function()
    assert result == "Function successfully executed!"


@pytest.mark.asyncio
async def test_debug_only_decorator_debug_disabled(mocker):
    # Mock the DEBUG setting as False
    mocker.patch.object(settings, "DEBUG", False)

    # Check that raised HTTPException with code 503
    with pytest.raises(HTTPException) as exc_info:
        await some_function()

    assert exc_info.value.status_code == 503
    assert exc_info.value.detail == "Feature not available in production mode"
