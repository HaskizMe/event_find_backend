from fastapi import APIRouter, HTTPException

from schemas.login_schema import LoginRequest, LoginResponse, VerifyLoginRequest
from schemas.signup_schema import SignUpRequest, SignUpResponse
from services.login_service import LoginService


router = APIRouter(prefix="/api/signup", tags=["Authentication"])

@router.post("/")
async def signup(signup: SignUpRequest):
    try:
        response = LoginService.signup_user(signup.email, signup.password, signup.username)
        return response
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    