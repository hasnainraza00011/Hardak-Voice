from telegram import Update
from telegram.ext import ContextTypes
from config import USDT_ADDRESS, EASYPAISA_NAME, EASYPAISA_NUMBER

async def deposit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 *Deposit Instructions:*\n\n"
        "🔸 *USDT (TRC20)*\n"
        f"📥 Address: `{USDT_ADDRESS}`\n\n"
        "🔸 *Easypaisa*\n"
        f"👤 Name: *{EASYPAISA_NAME}*\n"
        f"📱 Number: `{EASYPAISA_NUMBER}`\n\n"
        "📤 After sending payment, please upload the screenshot using the *Upload payment Ss* option.\n\n"
        "🕐 Your payment will be verified shortly.",
        parse_mode="Markdown"
    )
