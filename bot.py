from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1425412568:AAGs6R4wfShzW-6S_p1NpF61bkkQ-ZF7-wU")
API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "SongsDownloaderTgBot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
