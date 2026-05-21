from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(
    filters.command("admin") &
    filters.user(ADMINS)
)
async def admin_panel(_, message):

    text = """
🛠 𝘈𝘥𝘮𝘪𝘯 𝘗𝘢𝘯𝘦𝘭

/upload notes sem1 maths
/delete notes sem1 maths

/list
/stats

𝘜𝘴𝘦 𝘶𝘱𝘭𝘰𝘢𝘥 → 𝘵𝘩𝘦𝘯 𝘴𝘦𝘯𝘥 𝘗𝘋𝘍
"""

    await message.reply_text(text)
