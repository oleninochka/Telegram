from typing import List, Dict, Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from app.api.dto.event import EventResponse
from app.api.service import EventService
from app.view.state.user import EventStateGroup


class EventHandler:
    @staticmethod
    async def list_events(**kwargs) -> Dict[str, List[EventResponse]]:
        events = await EventService.list_events()
        return {"events": events.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, _: Any, dialog_manager: DialogManager, item_id: str):
        event = await EventService.find_by_id(item_id)
        if event.status != 200:
            await callback.message.reply(event.message)
            await dialog_manager.switch_to(EventStateGroup.menu)
        else:
            await dialog_manager.update({"select": event.as_json()})
            await dialog_manager.switch_to(EventStateGroup.select)

    @staticmethod
    async def render(dialog_manager: DialogManager, **kwargs):
        select = dialog_manager.dialog_data["select"]
        return EventResponse.parse(select["data"]).as_dict()
