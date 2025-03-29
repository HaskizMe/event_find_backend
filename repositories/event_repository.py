import random
import httpx
import json
import uuid


from schemas.event_schema import Event, EventsResponse, EventRequest


class EventRepository:

    @staticmethod
    def get_all_events() -> EventsResponse | None:
        try:
            with open("./db/events.json", "r") as file:
                data = json.load(file)  # this should be a list of event dicts
                events = [Event(**event) for event in data]
                return EventsResponse(count=len(events), results=events)
        except FileNotFoundError:
            raise Exception("Events file not found")
        
    @staticmethod
    def create_event(event: EventRequest, user_id: int) -> Event | None:
        try:
            with open("./db/events.json", "r") as file:
                data = json.load(file)

            # Generate a random numeric ID that isn't already used
            existing_ids = {e.get("id") for e in data if "id" in e}
            new_id = random.randint(1000, 9999)
            while new_id in existing_ids:
                new_id = random.randint(1000, 9999)

            # Create new Event with an ID and user_id
            event_data = event.dict()
            event_data["id"] = new_id
            event_data["user_id"] = user_id

            data.append(event_data)

            with open("./db/events.json", "w") as file:
                json.dump(data, file, indent=4)

            return Event(**event_data)

        except FileNotFoundError:
            raise Exception("Events file not found")
        except Exception as e:
            raise e