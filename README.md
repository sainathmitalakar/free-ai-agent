# 🧠 Free AI Agent

![AI Agent Banner](https://raw.githubusercontent.com/sainathmitalakar/free-ai-agent/main/static/ai-banner.png)

## Overview

**Free AI Agent** is a **real-time AI-powered dashboard** that integrates **Telegram** and **Discord** bots into a single web interface. It allows you to **send and receive messages from both platforms** through a sleek, hacker-style web UI.  

Think of it as your **centralized AI assistant** for multi-platform chatting, testing, and automation.

---

## Features

- ✅ **Multi-platform Chat**: Interact with both Telegram and Discord bots from one dashboard.
- ✅ **Real-time Message Sending**: Send messages instantly to Telegram groups/channels or Discord servers.
- ✅ **Slick Web UI**: Hacker-style, digital-themed interface for a modern dashboard look.
- ✅ **Local and Remote Ready**: Run locally or deploy to cloud platforms like **Render** or **Railway**.
- ✅ **Lightweight & Python Powered**: Built with Python, Flask, Discord.py, and Python Telegram Bot.

---

## Tech Stack

- **Python 3.13+**
- **Flask** – Web interface
- **Discord.py** – Discord bot integration
- **python-telegram-bot** – Telegram bot integration
- **Asyncio & Threading** – For simultaneous bot operations
- **HTML / CSS / JS** – Frontend dashboard design

---

## Project Structure

<img width="503" height="225" alt="image" src="https://github.com/user-attachments/assets/daf92c4d-96e0-448c-98f1-3234a1d9c7d7" />



---

## Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sainathmitalakar/free-ai-agent.git
cd free-ai-agent

2️⃣ Create a .env file
# Telegram
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
YOUR_CHAT_ID=your_telegram_chat_id

# Discord
DISCORD_BOT_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_discord_channel_id

Important: Keep .env private. Never push bot tokens to GitHub.
3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Dashboard
python web_ui.py


Visit: http://127.0.0.1:5000

Send messages to Telegram or Discord directly from the dashboard.

Security & Notes

Make sure your bot tokens are never pushed to public repositories.

GitHub’s push protection may block commits with secrets (like your .env file).

For live hosting, use services like Render or Railway that can run Python apps.

Contribution

Contributions are welcome! You can:

Add more platforms (Slack, WhatsApp, etc.)

Improve UI/UX with advanced dashboards

Integrate AI features for auto-replies

License

MIT License © 2025 Sainath Mitalakar

⚡ Tip: This project is perfect for DevOps engineers, AI enthusiasts, and bot developers to explore multi-platform messaging automation with a slick UI.



