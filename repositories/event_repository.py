from models.event_model import Event
from models.user_model import User
from schemas.event_schema import EventRequest, EventsResponse, EventResponse
from sqlalchemy.orm import Session

class EventRepository:
    def __init__(self, db):
        self.db: Session = db.get_session()

    def get_all_events(self) -> EventsResponse:
        events = self.db.query(Event).all()

        event_responses = [
            EventResponse(
                **event.__dict__,
                attendees=[user.id for user in event.attendees]
            )
            for event in events
        ]

        return EventsResponse(results=event_responses)

    def get_event_by_id(self, event_id: int) -> EventResponse | None:
        event = self.db.query(Event).filter_by(id=event_id).first()
        if not event:
            return None

        return EventResponse(
            **event.__dict__,
            attendees=[user.id for user in event.attendees]
        )

    def create_event(self, event: EventRequest, user_id: int) -> EventResponse:
        try:
            new_event = Event(**event.model_dump(), user_id=user_id)
            self.db.add(new_event)
            self.db.commit()
            self.db.refresh(new_event)
            return EventResponse.model_validate(new_event)
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error creating event: {e}")

    def set_attendance(self, event_id: int, user_id: int, attending: bool) -> Event:
        try:
            event = self.db.query(Event).filter_by(id=event_id).first()
            if not event:
                raise Exception("Event not found")

            user = self.db.query(User).filter_by(id=user_id).first()
            if not user:
                raise Exception("User not found")

            if attending:
                if user not in event.attendees:
                    event.attendees.append(user)
            else:
                if user in event.attendees:
                    event.attendees.remove(user)

            self.db.commit()
            self.db.refresh(event)
            return event
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating attendance: {e}")

    def delete_event(self, event_id: int):
        event = self.db.query(Event).filter_by(id=event_id).first()
        if event:
            self.db.delete(event)
            self.db.commit()