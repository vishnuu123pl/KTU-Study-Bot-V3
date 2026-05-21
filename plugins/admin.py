from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(
    filters.command("admin") &
    filters.user(ADMINS)
)
async def admin_panel(_, message):

    text = """
🛠 Admin Panel

/upload notes sem1 maths
/delete notes sem1 maths

/list
/stats

Use upload → then send PDF
"""

    await message.reply_text(text)
