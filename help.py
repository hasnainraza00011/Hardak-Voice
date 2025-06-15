from telegram import Update
from telegram.ext import ContextTypes

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 *Help Guide*\n\n"
        "🎙 *Voice Convert*: Send a voice message to convert it via Novita AI.\n"
        "💰 *Deposit Money*: Choose USDT or Easypaisa and send screenshot proof.\n"
        "🪙 *Balance*: View your current balance in USDT or PKR.\n"
        "📋 *Plans*: See our available voice plans.\n"
        "👥 *Referral*: Share your code to earn bonus.\n"
        "📤 *Upload Payment Ss*: Send screenshot to verify payment.\n\n"
        "For help, contact admin @ChoseYou_bot.",
        parse_mode="Markdown"
    )
