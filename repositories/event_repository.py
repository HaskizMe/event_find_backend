import httpx
import json

from schemas.event_schema import Event, EventResponse


class SWAPIRepository:
    # @staticmethod
    # async def get_all_films() -> FilmResponse | None:
    #     url = "https://swapi.dev/api/films/"
    #     async with httpx.AsyncClient() as client:
    #         response = await client.get(url)
    #         if response.status_code == 200:
    #             return FilmResponse(**response.json())
    #     return None
    
    @staticmethod
    def get_all_events() -> EventResponse | None:
        try:
            with open("./db/events.json", "r") as file:
                data = json.load(file)  # this should be a list of event dicts
                events = [Event(**event) for event in data]
                return EventResponse(count=len(events), results=events)
        except FileNotFoundError:
            raise Exception("Events file not found")