import os
from dotenv import load_dotenv
from fastapi import APIRouter
from schemas.api_key_schema import KeyResponse

load_dotenv()

router = APIRouter(prefix="/api/keys", tags=["Authorization"])

MAPBOX_PUBLIC_KEY = os.getenv("MAPBOX_PUBLIC_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@router.get("/mapbox", response_model=KeyResponse)
async def get_mapbox_key():
    return {"key": MAPBOX_PUBLIC_KEY}

@router.get("/weather", response_model=KeyResponse)
async def get_weather_key():
    return {"key": WEATHER_API_KEY}