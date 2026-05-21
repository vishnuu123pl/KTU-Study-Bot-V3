from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Client(
    "KTUStudyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=os.path.join(BASE_DIR, "plugins"))
)


async def main():

    await app.start()

    print("✅ Bot Started Successfully")

    for admin in ADMINS:
        try:
            await app.send_message(admin, "🔄 Bot Restarted Successfully")
        except Exception as e:
            print(e)

    await idle()
