from pydantic import BaseModel

class SignUpResponse(BaseModel):
    success: bool
    message: str

class SignUpRequest(BaseModel):
    email: str
    username: str
    password: str