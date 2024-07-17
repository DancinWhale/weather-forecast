from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.exceptions import IncorrectCityNameException
from app.weather.router import router as router_weather
from app.pages.router import router as router_pages


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_weather)
app.include_router(router_pages)

origins = [
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin"]
)


@app.exception_handler(IncorrectCityNameException)
async def custom_500_handler(_, __):
    return RedirectResponse("/pages/error")
