from app.config import RouteConfig


class ChallengeRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_challenges() -> str:
        return ChallengeRoute.route.url + '/select'

    @staticmethod
    def find_by_id(challenge_id: str) -> str:
        return ChallengeRoute.route.url + f'/select/{challenge_id}'

    @staticmethod
    def submit(challenge_id: str) -> str:
        return ChallengeRoute.route.url + f'/select/{challenge_id}/submit'
