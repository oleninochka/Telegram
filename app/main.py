import logging

from app import dp, bot
from app.handler.dialog.register import register_dialogs
from app.handler.router.register import register_routes

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def start():
    logger.info('started')
    try:
        dp.run_polling(bot)
    finally:
        logger.info('stopped')


def main():
    register_routes()
    register_dialogs()
    start()


if __name__ == '__main__':
    main()
