import requests
from src.data.mars_weather_model import get_mars_weather, upsert_mars_weather
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_URI = os.getenv('POSTGRES_URI')
NASA_API_KEY = os.getenv('NASA_API_KEY')
class MarsWeatherService:
    def fetch_weather_data_from_nasa(self):

        url = f"https://api.nasa.gov/insight_weather/?api_key={NASA_API_KEY}&feedtype=json&ver=1.0"

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
        
        for sol in requests.get("sol_keys", []):
            sol_data = requests[sol]

            # Crear instancia del modelo
            data = {
                "sol":int(sol),
                "average_temperature":sol_data.get("AT", {}).get("av",0),
                "max_temperature":sol_data.get("AT", {}).get("mx",0),
                "min_temperature":sol_data.get("AT", {}).get("mn",0),
                "season":sol_data.get("Season"),
                "month_ordinal":sol_data.get("Month_ordinal"),
                "date_start":datetime.fromisoformat(sol_data.get("First_UTC").replace("Z", "+00:00")) if sol_data.get("First_UTC") else None,
                "date_end":datetime.fromisoformat(sol_data.get("Last_UTC").replace("Z", "+00:00")) if sol_data.get("Last_UTC") else None
            }

            upsert_mars_weather(data)

       
    def get_weather_data(self, sol):
        

        data = get_mars_weather({"sol": sol})

        return data