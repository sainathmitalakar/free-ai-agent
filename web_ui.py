from flask import Flask, render_template, request, jsonify
import os
import asyncio
from telegram import Bot as TelegramBot
import discord
from discord.ext import commands
import threading
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Tokens
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("YOUR_CHAT_ID")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", 0))

# Telegram Bot
telegram_bot = TelegramBot(token=TELEGRAM_TOKEN)

# Discord Bot
intents = discord.Intents.default()
intents.message_content = True
discord_bot = commands.Bot(command_prefix="!", intents=intents)

@discord_bot.event
async def on_ready():
    print(f"Discord Bot ready: {discord_bot.user}")

# Flask
app = Flask(__name__)

# Keep last messages
messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send_msg():
    data = request.json
    msg = data.get("message", "")
    platform = data.get("platform", "")

    if platform == "telegram":
        asyncio.create_task(telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg))
    elif platform == "discord":
        channel = discord_bot.get_channel(DISCORD_CHANNEL_ID)
        if channel:
            asyncio.run_coroutine_threadsafe(channel.send(msg), discord_bot.loop)

    # Save locally for UI
    import datetime
    messages.insert(0, (platform, "You", msg, datetime.datetime.now().strftime("%H:%M:%S")))
    if len(messages) > 50:
        messages.pop()

    return jsonify({"ok": True, "message": msg})

# Run Discord in thread
def run_discord_bot():
    discord_bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    threading.Thread(target=run_discord_bot, daemon=True).start()
    app.run(port=5000)
