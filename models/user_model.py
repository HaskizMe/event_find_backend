# import random

# class User:
#     def __init__(self, email: str, username: str, password_hash: str, id: int = None):
#         self.id = id or random.randint(100000, 999999)  # 6-digit random ID just for now since we will be adding a database later
#         self.email = email
#         self.username = username
#         self.password_hash = password_hash



# models/user_model.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    attending_events = relationship("Event", secondary="event_attendees", back_populates="attendees")