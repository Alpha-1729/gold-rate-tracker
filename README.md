# 💰 Gold Rate Tracker

Monitors Kerala gold prices and sends Telegram notifications when prices change.

## 🚀 Quick Setup (3 Steps)

### Step 1: Clone the Project

```bash
git clone https://github.com/yourusername/gold-rate-tracker.git
cd gold-rate-tracker
```

### Step 2: Create .env File

Create a file named `.env` in the project folder and add:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

**How to get credentials:**
- **Bot Token**: Message [@BotFather](https://t.me/botfather) → Send `/newbot`
- **Chat ID**: Message [@userinfobot](https://t.me/userinfobot)

### Step 3: Run with Docker

```bash
docker compose up -d --build
```

**That's it!** Check logs:

```bash
docker compose logs -f
```

## 📊 You'll Receive Messages Like This

```
💰 Gold Rate in Kerala - 02 Jan 2026
• 22K (1g): ₹12,485
• 24K (1g): ₹13,620
```

## 📝 License

MIT License

---

⭐ **Star this repo if you find it useful!**
