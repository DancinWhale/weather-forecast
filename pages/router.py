from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.weather.router import get_weather

router = APIRouter(
    prefix="/pages",
    tags=["Frontend"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/weather")
async def get_weather_page(
        request: Request,
        weather=Depends(get_weather)
):
    return templates.TemplateResponse(
        name="weather.html",
        context={"request": request, "weather": weather},
    )


@router.get("/")
async def get_main_page(
        request: Request,
):
    return templates.TemplateResponse(
        name="main.html",
        context={"request": request},
    )


@router.get("/error")
async def get_error(
        request: Request,
):
    return templates.TemplateResponse(
        name="error.html",
        context={"request": request},
    )