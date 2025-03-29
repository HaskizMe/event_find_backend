import os
from dotenv import load_dotenv
from fastapi import APIRouter

load_dotenv()

router = APIRouter(prefix="/api/keys", tags=["Authorization"])

MAPBOX_PUBLIC_KEY = os.getenv("MAPBOX_PUBLIC_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@router.get("/mapbox", response_model=str)
async def get_mapbox_key():
    return MAPBOX_PUBLIC_KEY


@router.get("/weather", response_model=str)
async def get_weather_key():
    return WEATHER_API_KEY