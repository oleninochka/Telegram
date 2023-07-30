import logging
from typing import Any

from aiogram.dispatcher import router
from aiogram.types.error_event import ErrorEvent

logger = logging.getLogger(__name__)


@router.errors()
async def error_handler(exception: ErrorEvent) -> Any:
    logger.info("Something went wrong")
    logger.exception(exception)
