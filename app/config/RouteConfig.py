from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class RouteConfig:
    url: str

    @staticmethod
    def load() -> RouteConfig:
        return RouteConfig(url=os.getenv("API_URL"))
