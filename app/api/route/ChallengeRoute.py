from app.config import RouteConfig


class ChallengeRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_challenges() -> str:
        return ChallengeRoute.route.url + "/challenge"

    @staticmethod
    def find_by_id(challenge_id: str) -> str:
        return ChallengeRoute.route.url + f"/challenge/{challenge_id}"

    @staticmethod
    def submit(challenge_id: str) -> str:
        return ChallengeRoute.route.url + f"/challenge/{challenge_id}/submit"
