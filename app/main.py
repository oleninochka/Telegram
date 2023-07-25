import logging

from app import dp, bot
from app.dialog import register_dialogs
from app.handler import register_handlers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def start():
    logger.info('started')
    try:
        dp.run_polling(bot)
    finally:
        logger.info('stopped')


def main():
    register_handlers()
    register_dialogs()
    start()


if __name__ == '__main__':
    main()
