from dataclasses import asdict
from typing import List, Dict, Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.api.dto.base import ApiResponse
from app.api.dto.team import TeamResponse, ParticipateRequest
from app.api.service import TeamService
from app.database.entity import User
from app.view.state import TeamStateGroup


class TeamHandler:
    @staticmethod
    async def list_teams(**kwargs) -> Dict[str, List[TeamResponse]]:
        teams = await TeamService.list_teams()
        return {'teams': teams.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: str):
        team = await TeamService.find_by_id(item_id)
        if team.status != 200:
            await callback.message.reply(team.message)
            await dialog_manager.switch_to(TeamStateGroup.menu)
        else:
            await dialog_manager.update({'select': team})
            await dialog_manager.switch_to(TeamStateGroup.select)

    @staticmethod
    async def render(dialog_manager: DialogManager, **kwargs):
        response: ApiResponse = dialog_manager.dialog_data['select']
        return asdict(response.data)

    @staticmethod
    async def participate(message: Message, input: MessageInput, dialog_manager: DialogManager):
        team: ApiResponse[TeamResponse] = dialog_manager.dialog_data['select']
        request = TeamHandler.participate_request(message)
        response = await TeamService.participate(team.data.id, request)
        await message.reply(response.message)
        await dialog_manager.switch_to(TeamStateGroup.menu)

    @staticmethod
    def participate_request(message: Message) -> ParticipateRequest:
        user: User = User.get_or_none(User.chat_id == message.chat.id)
        return ParticipateRequest(
            invite=message.text,
            userId=str(user.id),
        )
