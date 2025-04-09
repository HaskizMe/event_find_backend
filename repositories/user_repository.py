import json

from models.user_model import User

class UserRepository:
    def __init__(self, db):
        self.db = db.get_session()

    
    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
        

# class UserRepository:
#     @staticmethod
#     def get_user_by_email(email: str) -> User:
#         try:
#             with open("./db/users.json", "r") as file:
#                 data = json.load(file)
#                 for user in data["users"]:
#                     if user["email"] == email:
#                         return User(
#                             username=user["username"],
#                             email=user["email"],
#                             password_hash=user["password_hash"],
#                             id=user.get("id")
#                         )
#         except FileNotFoundError:
#             raise Exception("User file not found")
#         return None
    
#     @staticmethod
#     def create_user(user: User) -> User:
#         try:
#             with open("./db/users.json", "r") as file:
#                 data = json.load(file)
#                 data["users"].append(user.__dict__)
#             with open("./db/users.json", "w") as file:
#                 json.dump(data, file, indent=4)

#             return user
#         except FileNotFoundError:
#             raise Exception("User file not found")
#         except Exception as e:
#             raise Exception(f"Failed to create user: {str(e)}")
        

#     @staticmethod
#     def get_user_info(user_id: int):
#         try:
#             with open("./db/users.json", "r") as file:
#                 data = json.load(file)
#                 for user in data["users"]:
#                     if user.get("id") == user_id:
#                         return User(
#                             username=user["username"],
#                             email=user["email"],
#                             password_hash=user["password_hash"],
#                             id=user.get("id")
#                         )
#         except FileNotFoundError:
#             raise Exception("User file not found")
#         return None