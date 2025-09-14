from fastapi import Depends, FastAPI

from src.controllers import mars_weather_controller

app = FastAPI()

app.include_router(mars_weather_controller.router)
