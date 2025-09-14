from fastapi import APIRouter
from services.mars_weather_service import MarsWeatherService

class MarsWeatherController:
    def __init__(self):
        self.router = APIRouter()
        self.service = MarsWeatherService()
        self.router.add_api_route("/weather", self.get_weather, methods=["GET"])

    async def get_weather(self):
        weather_data = await self.service.fetch_weather_data()
        return weather_data