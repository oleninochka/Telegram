from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, ScrollingGroup, Select, Cancel
from aiogram_dialog.widgets.text import Const, Format

from app.controller.handler.user import TeamHandler
from app.view.state.user import TeamStateGroup
from app.view.static import StaticLoader
from app.widgets import back

menu = Window(
    StaticLoader.template("team/list"),
    ScrollingGroup(
        Select(
            Format("{item.name}"),
            item_id_getter=attrgetter("id"),
            items="teams",
            id="team_select",
            on_click=TeamHandler.select,
        ),
        width=1,
        height=5,
        id="team_group",
    ),
    Cancel(back, id="back"),
    getter=TeamHandler.list_teams,
    state=TeamStateGroup.menu,
)

select = Window(
    Format("{name}"),
    Row(
        SwitchTo(back, id="back", state=TeamStateGroup.menu),
        SwitchTo(Const("🤝 Присоединиться"), id="submit", state=TeamStateGroup.participate),
    ),
    getter=TeamHandler.render,
    state=TeamStateGroup.select,
)

participate = Window(
    Const("Введите инвайт-токен:"),
    SwitchTo(back, id="back", state=TeamStateGroup.select),
    MessageInput(TeamHandler.participate),
    state=TeamStateGroup.participate,
)
