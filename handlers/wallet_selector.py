from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.process_query import fetch_and_summarize

# Simple in-memory store for wallet addresses
wallet_map = {}

OPTIONS = [
    "DeFi Portfolio",
    "NFT Portfolio",
    "ERC20 Portfolio",
    "Wallet Score",
    "Wallet Label",
    "Wallet Metrics"
]

async def ask_wallet_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Please enter a wallet address you'd like to analyze:")
    context.chat_data["next"] = "get_wallet"  # Initialize next step

async def handle_wallet_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    wallet = update.message.text.strip()

    if wallet.startswith("0x") and len(wallet) == 42:
        wallet_map[user_id] = wallet
        keyboard = ReplyKeyboardMarkup([[opt] for opt in OPTIONS], one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text("Choose what you'd like to analyze:", reply_markup=keyboard)
        context.chat_data["next"] = "select_option"
    else:
        await update.message.reply_text("Invalid wallet address. Please try again (starts with 0x, length 42).")
        context.chat_data["next"] = "get_wallet"

async def handle_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    selection = update.message.text.strip()
    wallet = wallet_map.get(user_id)

    if not wallet:
        await update.message.reply_text("Please send the wallet address first using /start")
        context.chat_data["next"] = "get_wallet"
        return

    await update.message.reply_text(f"🔍 Fetching {selection} data for wallet `{wallet}`...", parse_mode="Markdown")
    summary = await fetch_and_summarize(wallet, selection)
    await update.message.reply_text(summary, parse_mode="Markdown")

    # Reset flow to accept another wallet if needed
    context.chat_data["next"] = "get_wallet"

# Router that dispatches based on current step
async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    step = context.chat_data.get("next", "get_wallet")

    if step == "get_wallet":
        return await handle_wallet_input(update, context)
    elif step == "select_option":
        return await handle_selection(update, context)
