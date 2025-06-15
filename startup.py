from aiogram import types
from loader import dp

@dp.message_handler(commands=["start"])
async def welcome_menu(msg: types.Message):
    buttons = [
        [types.KeyboardButton("💰 Deposit Money"), types.KeyboardButton("📦 Plans")],
        [types.KeyboardButton("🎙️ Voice Convert"), types.KeyboardButton("📊 Balance")],
        [types.KeyboardButton("👥 Referral"), types.KeyboardButton("🖼️ Upload Payment Ss")]
    ]
    keyboard = types.ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await msg.answer("👋 Welcome to ChoseYou Bot!", reply_markup=keyboard)
  
