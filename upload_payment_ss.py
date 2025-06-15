from telegram import Update
from telegram.ext import ContextTypes
import os

async def proof_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        proof_dir = "payment_proofs"
        os.makedirs(proof_dir, exist_ok=True)
        file_path = f"{proof_dir}/{user.id}_{photo_file.file_id}.jpg"
        await photo_file.download_to_drive(file_path)
        await update.message.reply_text("✅ *Payment Ss received!*\nWe’ll verify it shortly.", parse_mode="Markdown")
    else:
        await update.message.reply_text("📸 Please send a screenshot image.")
