import asyncio
import logging
import telegram
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

logger = logging.getLogger(__name__)


def send_message(message: str) -> bool:
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.error("Telegram not configured - TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing")
        return False

    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        asyncio.run(bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode="HTML"))
        logger.info("Message sent successfully")
        return True
    except Exception as e:
        logger.exception(f"Failed to send message: {e}")
        return False
