from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import List



class Settings(BaseSettings):
    app_env: str
    allow_origins: str
    mapbox_public_key: str
    weather_api_key: str
    secret_key: str
    algorithm: str
    api_gateway_token: str
    database_user: str
    database_password: str
    database_host: str
    database_port: int = 5432
    database_name: str

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"
    
    @property
    def allow_origins_list(self) -> List[str]:
        return [origin.strip().rstrip("/") for origin in self.allow_origins.split(",")]

    class Config:
        env_file = ".env"


settings = Settings()