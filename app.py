import os
import logging
import asyncio
from dotenv import load_dotenv

# Discord imports
import discord
from discord.ext import commands

# Telegram imports
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Local AI and utils
from llm_local import ask_ai
from utils import save_message

# -------------------- Load Environment --------------------
load_dotenv(r"D:\AI Agent\free-ai-agent\.env")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("YOUR_CHAT_ID")

if not DISCORD_TOKEN:
    raise ValueError("⚠️ DISCORD_TOKEN not found in .env file")
if not TELEGRAM_TOKEN:
    raise ValueError("⚠️ TELEGRAM_BOT_TOKEN not found in .env file")
if not TELEGRAM_CHAT_ID:
    raise ValueError("⚠️ YOUR_CHAT_ID not found in .env file")

logging.basicConfig(level=logging.INFO)

# -------------------- Discord Bot --------------------
intents = discord.Intents.default()
intents.message_content = True  # Required to read messages
discord_bot = commands.Bot(command_prefix="!", intents=intents)

@discord_bot.event
async def on_ready():
    print(f"✅ Discord bot logged in as {discord_bot.user} and ready!")

@discord_bot.event
async def on_message(message):
    if message.author == discord_bot.user:
        return
    logging.info(f"Discord received: {message.content}")
    response = ask_ai(f"Reply like Sainath Mitalakar: {message.content}")
    await message.channel.send(response)
    save_message("discord", message.content, response)

# -------------------- Telegram Bot --------------------
async def telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        user_msg = update.message.text
        logging.info(f"Telegram received: {user_msg}")
        ai_response = ask_ai(f"Reply like Sainath Mitalakar: {user_msg}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ai_response)
        save_message("telegram", user_msg, ai_response)

def run_telegram_bot():
    """Runs Telegram bot safely on Python 3.13"""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, telegram_reply))
    print("✅ Telegram bot is running and waiting for messages...")
    app.run_polling()  # Handles event loop internally

# -------------------- Run Both Bots --------------------
def main():
    loop = asyncio.get_event_loop()

    # Run Discord in the event loop
    loop.create_task(discord_bot.start(DISCORD_TOKEN))
    # Run Telegram bot in executor to avoid loop conflicts
    loop.run_in_executor(None, run_telegram_bot)

    print("✅ Both Discord and Telegram bots are running!")
    loop.run_forever()

if __name__ == "__main__":
    main()
