from typing import List, Dict, Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.api.dto.base import ApiResponse
from app.api.dto.challenge import ChallengeResponse, SubmitRequest
from app.api.service import ChallengeService
from app.database import User
from app.view.state import ChallengeStateGroup


class ChallengeHandler:
    @staticmethod
    async def list_challenges(**kwargs) -> Dict[str, List[ChallengeResponse]]:
        challenges = await ChallengeService.list_challenges()
        return {'challenges': challenges.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: str):
        challenge = await ChallengeService.find_by_id(item_id)
        if challenge.status != 200:
            await callback.message.reply(challenge.message)
            await dialog_manager.switch_to(ChallengeStateGroup.menu)
        else:
            await dialog_manager.update({'select': challenge.as_json()})
            await dialog_manager.switch_to(ChallengeStateGroup.select)

    @staticmethod
    async def render(dialog_manager: DialogManager, **kwargs):
        select = dialog_manager.dialog_data['select']
        return ChallengeResponse.parse(select['data']).as_dict()

    @staticmethod
    async def submit(message: Message, input: MessageInput, dialog_manager: DialogManager):
        select = dialog_manager.dialog_data['select']
        challenge = ChallengeResponse.parse(select['data'])
        request = ChallengeHandler.submit_request(message)
        response = await ChallengeService.submit(challenge.id, request)
        await message.reply(response.message)
        await dialog_manager.switch_to(ChallengeStateGroup.menu)

    @staticmethod
    def submit_request(message: Message):
        user: User = User.get_or_none(User.chat_id == message.chat.id)
        return SubmitRequest(
            userId=str(user.id),
            flag=message.text,
        )
