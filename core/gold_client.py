import logging
import requests
from datetime import datetime
from dataclasses import dataclass
from config import API_BASE_URL, API_TOKEN, API_CITY, API_TIMEFRAME, API_REQUEST_HEADERS, API_TIMEOUT_SECONDS

logger = logging.getLogger(__name__)


@dataclass
class GoldPrice:
    """Gold price data model"""

    date: str
    gold_22k: str
    gold_24k: str

    def __str__(self) -> str:
        return f"Gold Price {self.date}, 22K: ₹{self.gold_22k}, 24K: ₹{self.gold_24k}"

    def to_dict(self) -> dict:
        return {"date": self.date, "gold_22k": self.gold_22k, "gold_24k": self.gold_24k}


def fetch_latest_price() -> GoldPrice | None:
    """Get latest Kerala gold price"""
    try:
        url = f"{API_BASE_URL}?token={API_TOKEN}&city={API_CITY}&timeframe={API_TIMEFRAME}"
        print(url)

        logger.info(f"Fetching gold prices for {API_CITY}")

        response = requests.get(url, headers=API_REQUEST_HEADERS, timeout=API_TIMEOUT_SECONDS)

        response.raise_for_status()

        data = response.json()
        latest = data[-1]

        result = GoldPrice(date=latest["on_date"], gold_22k=latest["22_c_1g"], gold_24k=latest["24_c_1g"])

        logger.info(f"✓ {result.date}: 22K ₹{result.gold_22k} | 24K ₹{result.gold_24k}")
        return result

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return None


def has_price_changed(current: GoldPrice, previous: GoldPrice) -> bool:
    """Check if price has changed"""
    return current.gold_22k != previous.gold_22k or current.gold_24k != previous.gold_24k


def format_price_message(current: GoldPrice) -> str:
    """Format current price message for Telegram"""
    date_obj = datetime.strptime(current.date, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%d %b %Y")
    return (
        f"💰 <b>Gold Rate in Kerala - {formatted_date}</b>\n"
        f"• 22K (1g): ₹{current.gold_22k}\n"
        f"• 24K (1g): ₹{current.gold_24k}"
    )
