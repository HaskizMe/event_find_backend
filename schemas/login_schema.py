from pydantic import BaseModel

# Define request model
class LoginRequest(BaseModel):
    email: str
    password: str

class VerifyLoginRequest(BaseModel):
    jwt_token: str

class LoginResponse(BaseModel):
    success: bool
    jwt_token: str|None = None
    mapbox_token: str|None = None
    weather_token: str|None = None
    username: str|None = None
    email: str|None = None
    user_id: int|None = None

    