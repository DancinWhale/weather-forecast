from httpx import AsyncClient


async def test_get_main_page(ac: AsyncClient):
    response = await ac.get("/pages")
    assert response.status_code == 200


async def test_get_error(ac: AsyncClient):
    response = await ac.get("/pages/error")
    assert response.status_code == 200
