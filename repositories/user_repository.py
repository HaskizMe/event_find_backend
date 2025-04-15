from models.user_model import User
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, db):
        self.db: Session = db.get_session()

    def get_user_by_email(self, email: str) -> User | None:
        try:
            return self.db.query(User).filter(User.email == email).first()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Failed to fetch user by email: {str(e)}")

    def create_user(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Failed to create user: {str(e)}")

    def get_user_info(self, user_id: int) -> User | None:
        try:
            return self.db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Failed to fetch user info: {str(e)}")