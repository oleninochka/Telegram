from operator import attrgetter
from typing import List, Dict

from aiogram.types import Chat

from app.api.dto.score import UserScoreResponse, TeamScoreResponse
from app.api.service import ScoreService, UserService
from app.database import User


class ScoreHandler:
    @staticmethod
    async def profile_score(event_chat: Chat, **kwargs) -> Dict:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        profile = await ScoreService.profile_score(user.id)
        return profile.data.as_json()

    @staticmethod
    async def user_scoreboard(event_chat: Chat, **kwargs) -> Dict[str, List[UserScoreResponse]]:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        users = await ScoreService.user_scoreboard()
        rating = users.data.content
        ids = list(map(attrgetter("user.id"), rating))
        place = ids.index(user.id) + 1 if user.id in ids else "∞"
        return {"users": rating[:10], "place": place}

    @staticmethod
    async def team_scoreboard(event_chat: Chat, **kwargs) -> Dict[str, List[TeamScoreResponse]]:
        user = await UserService.find_by_chat_id(event_chat.id)
        team = user.data.team
        teams = await ScoreService.team_scoreboard()
        rating = teams.data.content
        ids = list(map(attrgetter("team.id"), rating))
        place = ids.index(team.id) + 1 if team is not None and team.id in ids else "∞"
        return {"teams": rating[:10], "place": place}
