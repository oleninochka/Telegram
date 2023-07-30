from app.config import RouteConfig


class TeamRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_teams() -> str:
        return TeamRoute.route.url + "/team"

    @staticmethod
    def find_by_id(team_id: str) -> str:
        return TeamRoute.route.url + f"/team/{team_id}"

    @staticmethod
    def participate(team_id: str) -> str:
        return TeamRoute.route.url + f"/team/{team_id}/participant"
