from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "KTUStudyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def main():
    await app.start()
    print("✅ Bot Started")
    await idle()
    await app.stop()
