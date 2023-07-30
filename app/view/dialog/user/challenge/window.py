from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, ScrollingGroup, Select, Cancel, Checkbox
from aiogram_dialog.widgets.text import Const

from app.controller.handler.user import ChallengeHandler
from app.widgets import back
from app.view.state.user import ChallengeStateGroup
from app.view.static import StaticLoader

menu = Window(
    StaticLoader.template("challenge/list"),
    ScrollingGroup(
        Select(
            StaticLoader.template("challenge/preview"),
            item_id_getter=attrgetter("id"),
            items="challenges",
            id="challenge_select",
            on_click=ChallengeHandler.select,
        ),
        width=1,
        height=5,
        id="challenge_group",
    ),
    Row(
        Cancel(back, id="back"),
        Checkbox(
            Const("Скрыть решенные"),
            Const("Показать решенные"),
            id="toggle_solved",
            default=True,
            on_state_changed=ChallengeHandler.toggle_solved,
        ),
    ),
    getter=ChallengeHandler.list_challenges,
    state=ChallengeStateGroup.menu,
)

select = Window(
    StaticLoader.template("challenge/challenge"),
    Row(
        SwitchTo(back, id="back", state=ChallengeStateGroup.menu),
        SwitchTo(
            Const("🚩 Сдать флаг"), id="submit", state=ChallengeStateGroup.submit, when=ChallengeHandler.is_not_solved
        ),
    ),
    getter=ChallengeHandler.render,
    state=ChallengeStateGroup.select,
)

submit = Window(
    Const("Введите флаг:"),
    SwitchTo(back, id="back", state=ChallengeStateGroup.select),
    MessageInput(ChallengeHandler.submit),
    state=ChallengeStateGroup.submit,
)
