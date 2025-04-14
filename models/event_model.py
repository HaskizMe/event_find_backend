# models/event_model.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import Base

# Association table
event_attendees = Table(
    'event_attendees',
    Base.metadata,
    Column('event_id', ForeignKey('events.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True)
)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    country = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    attendees = relationship("User", secondary=event_attendees, back_populates="attending_events")