from pyrogram import Client as Bot
from pytgcalls import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()

from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# Sabse pehle ise call karein
keep_alive()

# Aapka purana code yahan se shuru hoga...
from pyrogram import Client
# ... baki code
