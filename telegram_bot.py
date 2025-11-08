import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
from llm_local import ask_ai
from utils import save_message

# Load environment
load_dotenv(r"D:\AI Agent\free-ai-agent\.env")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("YOUR_CHAT_ID")

if not TOKEN:
    raise ValueError("⚠️ TELEGRAM_BOT_TOKEN not found in .env file")
if not CHAT_ID:
    raise ValueError("⚠️ YOUR_CHAT_ID not found in .env file")

logging.basicConfig(level=logging.INFO)

# --- Handler ---
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        user_msg = update.message.text
        logging.info(f"Received: {user_msg}")
        ai_response = ask_ai(f"Reply like Sainath Mitalakar: {user_msg}")
        logging.info(f"AI Response: {ai_response}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ai_response)
        save_message("telegram", user_msg, ai_response)

# --- Optional direct message sender ---
async def send_message_async(msg: str):
    app = ApplicationBuilder().token(TOKEN).build()
    async with app:
        await app.bot.send_message(chat_id=CHAT_ID, text=msg)

def send_telegram_message(msg: str):
    import asyncio
    asyncio.run(send_message_async(msg))

# --- Run bot ---
if __name__ == "__main__":
    # Create and run the application directly (handles event loop internally)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("✅ Telegram bot is running and waiting for messages...")
    # Do NOT use asyncio.run() here
    app.run_polling()  # <-- THIS is Python 3.13 safe
