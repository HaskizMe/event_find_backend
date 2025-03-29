from pydantic import BaseModel

class SignUpRequest(BaseModel):
    success: bool
    message: str