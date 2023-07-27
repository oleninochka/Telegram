from __future__ import annotations

import os
from dataclasses import dataclass

from aiogram import Bot


@dataclass
class BotConfig:
    token: str
    parse_mode: str = 'HTML'

    @staticmethod
    def load() -> BotConfig:
        token = os.getenv('BOT_TOKEN').replace('"', '')
        return BotConfig(token=token)

    @property
    def bot(self) -> Bot:
        return Bot(
            token=self.token,
            parse_mode=self.parse_mode,
        )
