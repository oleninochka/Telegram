from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Radio, Cancel
from aiogram_dialog.widgets.text import Const, Format

from app.api.dto.support import SupportChannel
from app.controller.handler.user import SupportHandler
from app.widgets import back
from app.view.state.user import SupportStateGroup


async def get_data(**kwargs):
    return {"channels": list(SupportChannel)}


menu = Window(
    Const("Напишите о проблеме и выберете категорию:"),
    Radio(
        Format("🔘 {item.value}"),
        Format("⚪️ {item.value}"),
        id="tags",
        item_id_getter=attrgetter("name"),
        items="channels",
        on_state_changed=SupportHandler.set_channel,
    ),
    Cancel(back, id="back"),
    MessageInput(SupportHandler.submit),
    state=SupportStateGroup.menu,
    getter=get_data,
)
