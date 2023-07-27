import nest_asyncio
from aiogram import Dispatcher

from app.config import BotConfig, RedisConfig, DatabaseConfig

nest_asyncio.apply()

db = DatabaseConfig.load().connection
storage = RedisConfig.load().storage
dp = Dispatcher(storage=storage)

bot = BotConfig.load().bot
