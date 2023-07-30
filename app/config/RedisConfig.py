from __future__ import annotations

import os
from dataclasses import dataclass

from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio.client import Redis


@dataclass
class RedisConfig:
    host: str
    port: int

    @staticmethod
    def load() -> RedisConfig:
        return RedisConfig(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
        )

    @property
    def storage(self) -> RedisStorage:
        redis = Redis(host=self.host, port=self.port)
        return RedisStorage(redis, key_builder=DefaultKeyBuilder(with_destiny=True))
