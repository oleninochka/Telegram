from typing import List, Dict

from aiogram.types import Chat

from app.api.dto.score import UserScoreResponse, TeamScoreResponse
from app.api.service import ScoreService
from app.database import User


class ScoreHandler:
    @staticmethod
    async def profile_score(event_chat: Chat, **kwargs) -> Dict:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        profile = await ScoreService.profile_score(user.id)
        return profile.data.as_json()

    @staticmethod
    async def user_scoreboard(**kwargs) -> Dict[str, List[UserScoreResponse]]:
        users = await ScoreService.user_scoreboard()
        return {'users': users.data.content}

    @staticmethod
    async def team_scoreboard(**kwargs) -> Dict[str, List[TeamScoreResponse]]:
        teams = await ScoreService.team_scoreboard()
        return {'teams': teams.data.content}
