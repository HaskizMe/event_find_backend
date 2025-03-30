from fastapi import APIRouter, HTTPException, Depends, Request
import os
from dotenv import load_dotenv

from schemas.login_schema import LoginRequest, LoginResponse, VerifyLoginRequest
from services.login_service import LoginService
from utils.auth_utility import get_current_user_id 



router = APIRouter(prefix="/api", tags=["Authentication"])
load_dotenv()
MAPBOX_PUBLIC_KEY = os.getenv("MAPBOX_PUBLIC_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@router.post("/login/", response_model=LoginResponse)
async def login(login: LoginRequest):
    try:
        user, token = LoginService.get_login_token(login.email, login.password)

        return LoginResponse(
            success=True,
            jwt_token=token,
            username=user.username,
            email=user.email,
            user_id=user.id,
            weather_token=WEATHER_API_KEY,
            mapbox_token=MAPBOX_PUBLIC_KEY
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")

@router.post("/login/verify", response_model=LoginResponse)
async def verify(verify_request: VerifyLoginRequest):
    try:
        _ = LoginService.verify_token(verify_request.jwt_token)
        return LoginResponse(success=True, jwt_token=verify_request.jwt_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    

@router.get("/me", response_model=LoginResponse)
async def get_account(
    request: Request,
    user_id: int = Depends(get_current_user_id)
):
    try:
        # Get the raw token from the Authorization header
        auth_header = request.headers.get("Authorization")
        token = None
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        user = LoginService.get_user_info(user_id)

        return LoginResponse(
            success=True,
            username=user.username,
            email=user.email,
            user_id=user.id,
            jwt_token=token,  # ✅ Include the same token back if you want
            mapbox_token=MAPBOX_PUBLIC_KEY,
            weather_token=WEATHER_API_KEY
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))