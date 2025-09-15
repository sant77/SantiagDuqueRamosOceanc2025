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
        print("holaaa2")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error fetching data from NASA API: {response.status_code}")
            return response.raise_for_status()
        
        response_weather = response.json()

        for sol in response_weather.get("sol_keys", []):
        
            # Crear instancia del modelo
            data = {
                "sol":int(sol),
                "average_temperature":response_weather.get(sol,{}).get("AT", {}).get("av",0),
                "max_temperature":response_weather.get(sol,{}).get("AT", {}).get("mx",0),
                "min_temperature":response_weather.get(sol,{}).get("AT", {}).get("mn",0),
                "season":response_weather.get(sol,{}).get("Season"),
                "month_ordinal":response_weather.get(sol,{}).get("Month_ordinal"),
                "date_start":datetime.fromisoformat(response_weather.get(sol,{}).get("First_UTC").replace("Z", "+00:00")) if response_weather.get(sol,{}).get("First_UTC") else None,
                "date_end":datetime.fromisoformat(response_weather.get(sol,{}).get("Last_UTC").replace("Z", "+00:00")) if response_weather.get(sol,{}).get("Last_UTC") else None
            }
            print("holaaa")
            upsert_mars_weather(data)

       
    def get_weather_data(self, sol):
        

        data = get_mars_weather({"sol": sol})

        return data