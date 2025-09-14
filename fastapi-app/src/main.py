from fastapi import FastAPI
from controllers.mars_weather_controller import MarsWeatherController

app = FastAPI()

mars_weather_controller = MarsWeatherController()

app.include_router(mars_weather_controller.router)