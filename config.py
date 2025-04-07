from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str
    allow_origins: list[AnyHttpUrl] 
    mapbox_public_key: str
    weather_api_key: str
    secret_key: str
    algorithm: str
    api_gateway_token: str

    class Config:
        env_file = ".env"


settings = Settings()