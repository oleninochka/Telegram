import asyncio
from typing import List, Dict, Any

from aiogram.types import Message, Chat, CallbackQuery
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
        return response.data.as_json()

    @staticmethod
    async def link_telegram(message: Message, input: MessageInput, dialog_manager: DialogManager):
        request = UserHandler.link_telegram_request(message)
        response = await UserService.link_telegram(request)
        if response.status != 409:
            await message.reply(response.message)
        if response.status in (200, 409):
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
        User.create(
            id=response.data.id,
            telegram_id=message.from_user.id,
            chat_id=message.chat.id,
        )

    @staticmethod
    def not_in_team(data: Dict, widget: Whenable, manager: DialogManager):
        chat: Chat = data['middleware_data']['event_chat']
        loop = asyncio.get_event_loop()
        user = loop.run_until_complete(UserService.find_by_chat_id(chat.id))
        return user.data.team is None

    @staticmethod
    def is_admin(data: Dict, widget: Whenable, manager: DialogManager):
        chat: Chat = data['middleware_data']['event_chat']
        loop = asyncio.get_event_loop()
        user = loop.run_until_complete(UserService.find_by_chat_id(chat.id))
        return user.data.admin

    @staticmethod
    async def exit(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager):
        user: User = User.get_or_none(User.chat_id == callback.message.chat.id)
        user.delete_instance()
        await dialog_manager.done()
