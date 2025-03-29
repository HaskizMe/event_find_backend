import hashlib
from dotenv import load_dotenv
import os
import jwt
import datetime
from repositories.user_repository import UserRepository
from models.user_model import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

class LoginService:
    # Function to verify a jwt token
    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            # Decode token
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
        
    # Function to verify login from users.json
    @staticmethod
    def get_login_token(email: str, password: str) -> str:
        try:
            email = email.strip().lower()
            # Fetch user from database
            user = UserRepository.get_user_by_email(email)
            if not user:
                raise Exception("User not found")

            # Hash input password using SHA256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Verify password match
            if user.password_hash != hashed_password:
                raise Exception("Invalid credentials")
            
            user_payload = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }

            # Generate JWT token
            expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            token_payload = {
                "sub": user.username,  # Subject (user)
                "exp": expiration_time,  # Expiry time
                "user": user_payload  # Include role or other user attributes if needed
            }
            token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)

            return token
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")
        

    @staticmethod
    def signup_user(email: str, password: str, username: str) -> str:
        try:
            # Normalize inputs
            email = email.strip().lower()
            username = username.strip()

            # Check if the user already exists
            if UserRepository.get_user_by_email(email):
                raise Exception("Username already exists")

            # Hash the password before saving it
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # You can use the username for name or ask for a name separately
            new_user = User(username=username, email=email, password_hash=hashed_password)

            # Save the user using the repository
            UserRepository.create_user(new_user)

            # Return JWT token just like login
            return LoginService.get_login_token(email, password)

        except Exception as e:
            raise Exception(f"Signup failed: {str(e)}")