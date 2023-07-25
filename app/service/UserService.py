from dataclasses import asdict
from typing import List, Dict, Any

from aiogram.types import Message, Chat
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.backend.api import UserApi
from app.backend.dto.user import UserResponse, LinkTelegramRequest
from app.database.repository.UserRepository import UserRepository


class UserService:
    @staticmethod
    async def list_users(**kwargs) -> Dict[str, List[UserResponse]]:
        users = await UserApi.list_users()
        return {'users': users.data.content}

    @staticmethod
    async def find_by_id(event_chat: Chat, **kwargs) -> Dict[str, Any]:
        response = await UserApi.find_by_chat_id(event_chat.id)
        return asdict(response.data)

    @staticmethod
    async def link_telegram(message: Message, input: MessageInput, dialog_manager: DialogManager):
        request = LinkTelegramRequest.build(message)
        response = await UserApi.link_telegram(request)
        await message.reply(response.message)
        if response.status in (200, 409):
            await UserRepository.save_user(message)
            await UserService.open_menu(dialog_manager)

    @staticmethod
    async def open_menu(dialog_manager: DialogManager):
        from app.dialog import MenuDialog
        await dialog_manager.start(MenuDialog.StateGroup.menu)
