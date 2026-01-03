import os
import logging

# Gold API Configuration
API_BASE_URL = "https://www.goodreturns.in/gold-graph-data.html"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiJtZXRhbF9hcGlfd2ViIiwiaXNzIjoiZ29vZHJldHVybnNfYXBpIiwiaWF0IjoxNzY3Mzg0OTkwLCJleHAiOjE3NjczODY3OTB9.9J3IpULAIS_soG4icI3GArH8dIlx2ZodZ905jCSN8MM"
API_CITY = "kerala"
API_TIMEFRAME = "1W"
API_TIMEOUT_SECONDS = 10
API_REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# Logging Configuration
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Scheduler Configuration
RETRY_DELAY_SECONDS = 60
PRICE_CHECK_INTERVAL_HOURS = 2
