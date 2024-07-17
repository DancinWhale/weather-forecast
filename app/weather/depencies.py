import requests
import datetime
from app.config import API_KEY  # Ключ для погодной API берем из конфига


def get_city_data(city):  # Парсим данные с https://api.open-meteo.com, если их нет, то выдаем ошибку о некорректности города
    try:
        coordinates = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        )
        print(coordinates)
        coordinates_data = coordinates.json()[0]
        latitude = coordinates_data["lat"]
        longitude = coordinates_data["lon"]

        current_date = datetime.datetime.now(datetime.UTC)
        final_date = current_date + datetime.timedelta(hours=5)
        parsed_data = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&start_hour={str(current_date.isoformat())[:16]}&end_hour={str(final_date.isoformat())[:16]}"
        )
        return parsed_data.json()

    except Exception:
        return None


def weather_forecast(city):  # Заворачиваем наши данные в список словариков
    data = get_city_data(city)
    if data is None:  # Если данных нет, значит был введен несуществующий город, поэтому отдаем None
        return None
    weather = [{}] * 6

    # Нулевым элементом является погода на данный момент
    weather[0] = {
        "current_weather": {
            "city": city,
            "temperature": data["current"]["temperature_2m"],
            "humidity": data["current"]["relative_humidity_2m"],
            "wind_speed": data["current"]["wind_speed_10m"]
        }
    }

    # Далее заполняется погода в ближайшие пять часов
    for i in range(5):
        weather[i+1] = {
            "time": data["hourly"]["time"][i],
            "temperature": data["hourly"]["temperature_2m"][i],
            "humidity": data["hourly"]["relative_humidity_2m"][i],
            "wind_speed": data["hourly"]["wind_speed_10m"][i]
        }
    return weather
