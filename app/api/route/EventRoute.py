from app.config import RouteConfig


class EventRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_events() -> str:
        return EventRoute.route.url + "/event"

    @staticmethod
    def find_by_id(event_id: str) -> str:
        return EventRoute.route.url + f"/event/{event_id}"
