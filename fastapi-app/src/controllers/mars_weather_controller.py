from fastapi import APIRouter, HTTPException
from typing import Optional, Dict, List
from src.services.mars_weather_service import MarsWeatherService
from fastapi import APIRouter


router = APIRouter( prefix="/mars_weather",
                    tags=["mars_weather"])


@router.get("/get_data")
async def get_data_from_nasa_api():

    mars_weather_service = MarsWeatherService()

    mars_weather_service.fetch_weather_data_from_nasa()

    return {"message": "Datos obtenidos y almacenados correctamente"}
   
@router.post("/get_data_db")
async def get_data_from_db(data: dict):
    
    if not data or "id" not in data:
        raise HTTPException(status_code=400, detail="Tiene que haber un campo sol en el body")
    
    mars_weather_service = MarsWeatherService()

    get_data_from_db = mars_weather_service.get_weather_data(data.get("sol",0))

    response = get_data_from_db

    return response