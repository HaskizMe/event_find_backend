from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow only your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

class LoginRequest(BaseModel):
    username: str
    password: str

def verify_login(username: str, password: str):
    try:
        with open("./db/users.json") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    return True
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="File not found")
    
    return False


@app.post("/api/login")
def login(request: LoginRequest):
    if(verify_login(request.username, request.password)):
        return {"Success": "true"}
    raise HTTPException(status_code=401, detail="Invalid credentials")