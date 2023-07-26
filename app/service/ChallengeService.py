from dataclasses import asdict
from typing import List, Dict, Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.backend.api import ChallengeApi
from app.backend.dto.challenge import ChallengeResponse, SubmitRequest
from app.backend.dto.container import ApiResponse
from app.handler.state import ChallengeStateGroup


class ChallengeService:
    @staticmethod
    async def list_challenges(**kwargs) -> Dict[str, List[ChallengeResponse]]:
        challenges = await ChallengeApi.list_challenges()
        return {'challenges': challenges.data.content}

    @staticmethod
    async def find_by_id(**kwargs) -> Dict[str, List[ChallengeResponse]]:
        challenges = await ChallengeApi.list_challenges()
        return {'challenges': challenges.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: str):
        response = await ChallengeApi.find_by_id(item_id)
        if response.status != 200:
            await callback.message.reply(response.message)
            await dialog_manager.switch_to(ChallengeStateGroup.menu)
        else:
            await dialog_manager.update({'challenge': response})
            await dialog_manager.switch_to(ChallengeStateGroup.challenge)

    @staticmethod
    async def render_challenge(dialog_manager: DialogManager, **kwargs):
        response: ApiResponse = dialog_manager.dialog_data['challenge']
        return asdict(response.data)

    @staticmethod
    async def submit(message: Message, input: MessageInput, dialog_manager: DialogManager):
        challenge: ApiResponse[ChallengeResponse] = dialog_manager.dialog_data['challenge']
        request = SubmitRequest.build(message)
        response = await ChallengeApi.submit(challenge.data.id, request)
        await message.reply(response.message)
        await dialog_manager.switch_to(ChallengeStateGroup.menu)
