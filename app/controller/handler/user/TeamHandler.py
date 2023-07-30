from typing import List, Dict, Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.api.dto.team import TeamResponse, ParticipateRequest
from app.api.service import TeamService
from app.database import User
from app.view.state.user import TeamStateGroup


class TeamHandler:
    @staticmethod
    async def list_teams(**kwargs) -> Dict[str, List[TeamResponse]]:
        teams = await TeamService.list_teams()
        return {"teams": teams.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, _: Any, dialog_manager: DialogManager, item_id: str):
        team = await TeamService.find_by_id(item_id)
        if team.status != 200:
            await callback.message.reply(team.message)
            await dialog_manager.switch_to(TeamStateGroup.menu)
        else:
            await dialog_manager.update({"select": team.as_json()})
            await dialog_manager.switch_to(TeamStateGroup.select)

    @staticmethod
    async def render(dialog_manager: DialogManager, **kwargs):
        select = dialog_manager.dialog_data["select"]
        return TeamResponse.parse(select["data"]).as_dict()

    @staticmethod
    async def participate(message: Message, _: MessageInput, dialog_manager: DialogManager):
        select = dialog_manager.dialog_data["select"]
        team: TeamResponse = TeamResponse.parse(select["data"])
        request = TeamHandler.participate_request(message)
        response = await TeamService.participate(team.id, request)
        await message.reply(response.message)
        if response.status == 200:
            await dialog_manager.done()
        else:
            await dialog_manager.switch_to(TeamStateGroup.menu)

    @staticmethod
    def participate_request(message: Message) -> ParticipateRequest:
        user: User = User.get_or_none(User.chat_id == message.chat.id)
        return ParticipateRequest(
            invite=message.text,
            userId=str(user.id),
        )
