class UserRoute:
    url = "http://localhost:8000/api/v1"

    @staticmethod
    def list_users() -> str:
        return UserRoute.url + '/user'

    @staticmethod
    def find_by_chat_id(chat_id: int) -> str:
        return UserRoute.url + f'/user/telegram/{chat_id}'

    @staticmethod
    def link_telegram() -> str:
        return UserRoute.url + '/user/telegram'


class ChallengeRoute:
    url = "http://localhost:8000/api/v1"

    @staticmethod
    def list_challenges() -> str:
        return UserRoute.url + '/challenge'

    @staticmethod
    def find_by_id(challenge_id: str) -> str:
        return UserRoute.url + f'/challenge/{challenge_id}'

    @staticmethod
    def submit(challenge_id: str) -> str:
        return UserRoute.url + f'/challenge/{challenge_id}/submit'
