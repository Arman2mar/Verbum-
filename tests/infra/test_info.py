import pytest

@pytest.mark.asyncio
async def test_info(async_client):
    r = await async_client.get("/v1/info")
    assert r.status_code == 200
    data = r.json()
    assert "name" in data and "version" in data and "api_prefix" in data
