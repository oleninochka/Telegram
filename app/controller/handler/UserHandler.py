import asyncio
from dataclasses import asdict
from typing import List, Dict, Any

from aiogram.types import Message, Chat
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import MessageInput

from app.api.dto.user import UserResponse, LinkTelegramRequest
from app.api.service import UserService
from app.database import User
from app.view.state import MenuStateGroup


class UserHandler:
    @staticmethod
    async def list_users(**kwargs) -> Dict[str, List[UserResponse]]:
        users = await UserService.list_users()
        return {'users': users.data.content}

    @staticmethod
    async def find_by_id(event_chat: Chat, **kwargs) -> Dict[str, Any]:
        response = await UserService.find_by_chat_id(event_chat.id)
        return asdict(response.data)

    @staticmethod
    async def link_telegram(message: Message, input: MessageInput, dialog_manager: DialogManager):
        request = UserHandler.link_telegram_request(message)
        response = await UserService.link_telegram(request)
        if response.status != 409:
            await message.reply(response.message)
        if response.status == 200:
            await UserHandler.save_user(message)
            await dialog_manager.done()
            await dialog_manager.start(MenuStateGroup.menu)

    @staticmethod
    def link_telegram_request(message: Message) -> LinkTelegramRequest:
        return LinkTelegramRequest(
            token=message.text,
            telegramId=str(message.from_user.id),
            chatId=str(message.chat.id),
        )

    @staticmethod
    async def save_user(message: Message):
        response = await UserService.find_by_chat_id(message.chat.id)
        user = User(
            id=response.data.id,
            telegram_id=message.from_user.id,
            chat_id=message.chat.id,
        )
        user.save(force_insert=True)

    @staticmethod
    def not_in_team(data: Dict, widget: Whenable, manager: DialogManager):
        chat: Chat = data['middleware_data']['event_chat']
        loop = asyncio.get_event_loop()
        user = loop.run_until_complete(UserService.find_by_chat_id(chat.id))
        return user.data.team is None
