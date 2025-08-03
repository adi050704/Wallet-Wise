import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
from handlers.wallet_selector import ask_wallet_address, router
import os

logging.basicConfig(level=logging.INFO)

# Initialize bot with token from environment
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

# /start command triggers the wallet input prompt
app.add_handler(CommandHandler("start", ask_wallet_address))

# All text input is routed through the smart router
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, router))

print("🤖 Bot running...")
app.run_polling()
