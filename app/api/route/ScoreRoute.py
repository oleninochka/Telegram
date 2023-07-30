from app.config import RouteConfig


class ScoreRoute:
    route = RouteConfig.load()

    @staticmethod
    def profile_score(user_id: str) -> str:
        return ScoreRoute.route.url + f"/score/profile/{user_id}"

    @staticmethod
    def user_scoreboard() -> str:
        return ScoreRoute.route.url + "/score/user"

    @staticmethod
    def team_scoreboard() -> str:
        return ScoreRoute.route.url + "/score/team"
