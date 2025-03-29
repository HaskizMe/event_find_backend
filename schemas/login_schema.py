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
    