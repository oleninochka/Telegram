import logging

from app import dp, bot
from app.controller.router import register_routes
from app.view.dialog import register_dialogs

logging.basicConfig(level=logging.INFO)


def start():
    logger = logging.getLogger(__name__)
    logger.info("started")
    try:
        dp.run_polling(bot)
    finally:
        logger.info("stopped")


def main():
    register_routes()
    register_dialogs()
    start()


if __name__ == "__main__":
    main()
