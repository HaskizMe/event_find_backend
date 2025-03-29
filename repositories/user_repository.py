import json

from models.user_model import User



class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> User:
        try:
            with open("./db/users.json", "r") as file:
                data = json.load(file)
                for user in data["users"]:
                    if user["username"] == username:
                        return User(
                            username=user["username"],
                            name=user["name"],
                            password_hash=user["password_hash"],
                            id=user.get("id")  # ✅ this ensures you load the saved ID
                        )
        except FileNotFoundError:
            raise Exception("User file not found")
        return None
    
    @staticmethod
    def create_user(user: User) -> User:
        try:
            with open("./db/users.json", "r") as file:
                data = json.load(file)
                data["users"].append(user.__dict__)
            with open("./db/users.json", "w") as file:
                json.dump(data, file, indent=4)

            return user
        except FileNotFoundError:
            raise Exception("User file not found")
        except Exception as e:
            raise Exception(f"Failed to create user: {str(e)}")