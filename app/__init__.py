import nest_asyncio
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BotConfig

nest_asyncio.apply()
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = BotConfig.load().bot
