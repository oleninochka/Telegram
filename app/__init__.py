from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BotConfig
from app.filter.auth import authenticated

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = BotConfig.load().bot
