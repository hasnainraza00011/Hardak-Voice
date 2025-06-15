from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import sqlite3
from config import DB_NAME

async def balance_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    # Create user table if not exists
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    balance REAL DEFAULT 0,
                    currency TEXT DEFAULT 'USDT'
                 )''')
    conn.commit()

    # Fetch or initialize user balance
    c.execute("SELECT balance, currency FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    if not result:
        c.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        balance = 0
        currency = 'USDT'
    else:
        balance, currency = result

    keyboard = ReplyKeyboardMarkup(
        [["Show in USDT", "Show in PKR"]],
        resize_keyboard=True
    )

    await update.message.reply_text(
        f"💼 *Your Balance:*\n\n💰 {balance:.2f} {currency}\n\nChoose currency display option below:",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

    conn.close()

async def update_currency(user_id: int, currency: str):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET currency = ? WHERE user_id = ?", (currency, user_id))
    conn.commit()
    conn.close()
