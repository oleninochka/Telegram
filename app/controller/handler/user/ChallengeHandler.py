from typing import List, Dict, Any

from aiogram.types import Message, CallbackQuery, Chat
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import ManagedCheckboxAdapter

from app.api.dto.base import ApiResponse, PageResponse
from app.api.dto.challenge import ChallengeResponse, SubmitRequest
from app.api.service import ChallengeService
from app.database import User
from app.view.state.user import ChallengeStateGroup


class ChallengeHandler:
    @staticmethod
    async def list_challenges(
        event_chat: Chat, dialog_manager: DialogManager, **kwargs
    ) -> Dict[str, List[ChallengeResponse]]:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        challenges = await ChallengeService.list_challenges(user.id)
        challenges = ChallengeHandler.filter_solved_challenges(challenges, dialog_manager)
        return {"challenges": challenges.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, _: Any, dialog_manager: DialogManager, item_id: str):
        user: User = User.get_or_none(User.chat_id == callback.message.chat.id)
        challenge = await ChallengeService.find_by_id(item_id, user.id)
        if challenge.status != 200:
            await callback.message.reply(challenge.message)
            await dialog_manager.switch_to(ChallengeStateGroup.menu)
        else:
            await dialog_manager.update({"select": challenge.as_json()})
            await dialog_manager.switch_to(ChallengeStateGroup.select)

    @staticmethod
    async def toggle_solved(_: ChatEvent, checkbox: ManagedCheckboxAdapter, dialog_manager: DialogManager):
        await dialog_manager.update({"show_solved": checkbox.is_checked()})
        await dialog_manager.switch_to(ChallengeStateGroup.menu)

    @staticmethod
    async def render(dialog_manager: DialogManager, **kwargs):
        select = dialog_manager.dialog_data["select"]
        return ChallengeResponse.parse(select["data"]).as_dict()

    @staticmethod
    async def submit(message: Message, _: MessageInput, dialog_manager: DialogManager):
        select = dialog_manager.dialog_data["select"]
        challenge = ChallengeResponse.parse(select["data"])
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

    @staticmethod
    def is_not_solved(data: Dict, _: Whenable, __: DialogManager):
        challenge = ChallengeResponse.parse(data["dialog_data"]["select"]["data"])
        return not challenge.solved

    @staticmethod
    def filter_solved_challenges(
        challenges: ApiResponse[PageResponse[ChallengeResponse]], manager: DialogManager
    ) -> ApiResponse[PageResponse[ChallengeResponse]]:
        show_solved = manager.dialog_data.get("show_solved", True)
        if not show_solved:
            challenges.data.content = list(filter(lambda challenge: not challenge.solved, challenges.data.content))
        return challenges
