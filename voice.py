from aiogram import types
from loader import dp
import requests

API_KEY = "sk_FGtv5Uugh4nK14Vqsz9xCA4GUp14TFTOxuQlSfoSRk0"  # Replace with your real key

@dp.message_handler(commands=["voice"])
async def convert_to_voice(msg: types.Message):
    text = msg.get_args()
    if not text:
        return await msg.reply("❌ Please provide text to convert.")
    
    url = "https://api.novita.ai/api/tts"
    payload = {
        "text": text,
        "voice": "nova",
        "speed": 1.0,
        "volume": 1.0
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    r = requests.post(url, json=payload, headers=headers)
    if r.status_code == 200 and "audio_url" in r.json():
        await msg.answer_audio(r.json()["audio_url"])
    else:
        await msg.reply("⚠️ Failed to convert. Try again.")
