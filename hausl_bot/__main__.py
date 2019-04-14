import logging

from hausl_bot.telegram_handler import TelegramHandler

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    telegram = TelegramHandler()
