from telegram.ext import Updater, CommandHandler
from handlers.voice import voice_handler
from handlers.proof import proof_handler
from handlers.help import help_handler
from handlers.balance import balance_handler
from handlers.deposit import deposit_handler
from handlers.referral import referral_handler
from handlers.plans import plans_handler

from config import BOT_TOKEN

def start(update, context):
    update.message.reply_text("🎉 Welcome to @ChoseYou_bot!")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(voice_handler)
dp.add_handler(proof_handler)
dp.add_handler(help_handler)
dp.add_handler(balance_handler)
dp.add_handler(deposit_handler)
dp.add_handler(referral_handler)
dp.add_handler(plans_handler)

updater.start_polling()
updater.idle()
