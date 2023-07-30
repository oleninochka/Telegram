from app.config import RouteConfig


class UserRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_users() -> str:
        return UserRoute.route.url + "/user"

    @staticmethod
    def find_by_chat_id(chat_id: int) -> str:
        return UserRoute.route.url + f"/user/telegram/{chat_id}"

    @staticmethod
    def link_telegram() -> str:
        return UserRoute.route.url + "/user/telegram"
