# import random
# import httpx
# import json
# import uuid


# from schemas.event_schema import Event, EventsResponse, EventRequest


# class EventRepository:

#     @staticmethod
#     def get_all_events() -> EventsResponse | None:
#         try:
#             with open("./db/events.json", "r") as file:
#                 data = json.load(file)  # this should be a list of event dicts
#                 events = [Event(**event) for event in data]
#                 return EventsResponse(count=len(events), results=events)
#         except FileNotFoundError:
#             raise Exception("Events file not found")
        
#     @staticmethod
#     def get_event_by_id(event_id: int) -> Event | None:
#         try:
#             with open("./db/events.json", "r") as file:
#                 data = json.load(file)

#             for event in data:
#                 if event.get("id") == event_id:
#                     return Event(**event)

#             return None  # Event not found

#         except FileNotFoundError:
#             raise Exception("Events file not found")
#         except Exception as e:
#             raise e
        
#     @staticmethod
#     def create_event(event: EventRequest, user_id: int) -> Event | None:
#         try:
#             with open("./db/events.json", "r") as file:
#                 data = json.load(file)

#             # Generate a random numeric ID that isn't already used
#             existing_ids = {e.get("id") for e in data if "id" in e}
#             new_id = random.randint(1000, 9999)
#             while new_id in existing_ids:
#                 new_id = random.randint(1000, 9999)

#             # Create new Event with an ID and user_id
#             event_data = event.dict()
#             event_data["id"] = new_id
#             event_data["user_id"] = user_id
#             event_data["attendees"] = []

#             data.append(event_data)

#             with open("./db/events.json", "w") as file:
#                 json.dump(data, file, indent=4)

#             return Event(**event_data)

#         except FileNotFoundError:
#             raise Exception("Events file not found")
#         except Exception as e:
#             raise e
        
#     @staticmethod
#     def setAttending(event_id: int, user_id: int, attending: bool) -> Event | None:
#         try:
#             with open("./db/events.json", "r") as file:
#                 data = json.load(file)

#             for event in data:
#                 if event.get("id") == event_id:
#                     # Ensure "attendees" field exists
#                     event["attendees"] = event.get("attendees", [])

#                     if attending:
#                         if user_id not in event["attendees"]:
#                             event["attendees"].append(user_id)
#                     else:
#                         if user_id in event["attendees"]:
#                             event["attendees"].remove(user_id)

#                     # Save the updated data
#                     with open("./db/events.json", "w") as file:
#                         json.dump(data, file, indent=4)

#                     return Event(**event)

#             return None  # Event not found

#         except FileNotFoundError:
#             raise Exception("Events file not found")
#         except Exception as e:
#             raise e
        

#     @staticmethod
#     def delete_event(event_id: int):
#         try:
#             with open("./db/events.json", "r") as file:
#                 events = json.load(file)

#             filtered = [event for event in events if event["id"] != event_id]

#             with open("./db/events.json", "w") as file:
#                 json.dump(filtered, file, indent=4)
#         except FileNotFoundError:
#             raise Exception("Events file not found")
#         except Exception as e:
#             raise e


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
        new_event = Event(**event.model_dump(), user_id=user_id)  # <- use your actual SQLAlchemy model
        self.db.add(new_event)
        self.db.commit()
        self.db.refresh(new_event)
        return EventResponse.model_validate(new_event) 

    def set_attendance(self, event_id: int, user_id: int, attending: bool) -> Event:
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

    def delete_event(self, event_id: int):
        event = self.db.query(Event).filter_by(id=event_id).first()
        if event:
            self.db.delete(event)
            self.db.commit()