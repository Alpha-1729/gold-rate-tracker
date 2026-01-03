import time
import logging
from core.telegram_client import send_message
from core.gold_client import fetch_latest_price, has_price_changed, format_price_message, GoldPrice
import config

logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT, datefmt=config.LOG_DATE_FORMAT)

# Lower httpx logging level to prevent sensitive information from appearing in logs
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def main():
    logger.info("🚀 Gold Rate Tracker Started")
    send_message("🚀 <b>Gold Rate Tracker Started</b>")

    previous_price: GoldPrice | None = None

    while True:
        try:
            current_price = fetch_latest_price()

            if not current_price:
                logger.warning("Failed to fetch price, retrying ...")
                time.sleep(config.RETRY_DELAY_SECONDS)
                continue

            if previous_price is None or has_price_changed(current_price, previous_price):
                message = format_price_message(current_price)
                send_message(message)
                logger.info("Price update sent successfully")
                previous_price = current_price
            else:
                logger.info("No price change detected")
        except Exception as e:
            logger.exception(f"Error: {e}")

        logger.info(f"Sleeping for {config.PRICE_CHECK_INTERVAL_HOURS} hours")
        time.sleep(config.PRICE_CHECK_INTERVAL_HOURS * 3600)


if __name__ == "__main__":
    main()
