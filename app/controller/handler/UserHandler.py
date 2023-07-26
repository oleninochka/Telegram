from dataclasses import asdict
from typing import List, Dict, Any

from aiogram.types import Message, Chat
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.api.dto.user import UserResponse, LinkTelegramRequest
from app.api.service import UserService
from app.database.repository.UserRepository import UserRepository
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
        await message.reply(response.message)
        if response.status in (200, 409):
            await UserRepository.save_user(message)
            await dialog_manager.start(MenuStateGroup.menu)

    @staticmethod
    def link_telegram_request(message: Message) -> LinkTelegramRequest:
        return LinkTelegramRequest(
            token=message.text,
            telegramId=str(message.from_user.id),
            chatId=str(message.chat.id),
        )
