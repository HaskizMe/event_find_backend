import random

class User:
    def __init__(self, username: str, name: str, password_hash: str, id: int = None):
        self.id = id or random.randint(100000, 999999)  # 6-digit random ID just for now since we will be adding a database later
        self.username = username
        self.name = name
        self.password_hash = password_hash