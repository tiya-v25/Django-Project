import os
import django
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from core.models import TelegramUser  

logging.basicConfig(level=logging.INFO)
print("Telegram Bot is starting...")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    username = user.username or user.first_name or f"id_{user.id}"

    await sync_to_async(TelegramUser.objects.get_or_create)(username=username)
    await update.message.reply_text(f"Hi {username}, you're now registered!")

def main():
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise Exception("TELEGRAM_BOT_TOKEN is missing in .env file")

    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", start))

    print("Polling started!")
    app.run_polling()

if __name__ == "__main__":
    main()
