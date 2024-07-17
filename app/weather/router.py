from app.exceptions import IncorrectCityNameException
from app.weather.depencies import weather_forecast
from fastapi import APIRouter

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


# Получение погоды на данное время и на ближайшие пять часов вперед при условии, что город корректен
@router.get("")
async def get_weather(city):
    weather = weather_forecast(city)
    if weather is None:
        raise IncorrectCityNameException
    return weather

