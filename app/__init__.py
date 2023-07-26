import nest_asyncio
from aiogram import Dispatcher

from app.config import BotConfig, RedisConfig

nest_asyncio.apply()
storage = RedisConfig.load().storage
dp = Dispatcher(storage=storage)
bot = BotConfig.load().bot
