from fastapi import APIRouter, HTTPException

from schemas.login_schema import LoginRequest, LoginResponse, VerifyLoginRequest
from services.login_service import LoginService


router = APIRouter(prefix="/api/signup", tags=["Authentication"])

@router.post("/", response_model=LoginResponse)
async def signup(login: LoginRequest):
    try:
        token = LoginService.signup_user(login.username, login.password)
        return LoginResponse(success=True, jwt_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    