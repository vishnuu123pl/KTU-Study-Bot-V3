from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

START_TEXT = """
🎓 Welcome to KTU Study Bot

Your smart study companion for KTU students.

📚 Notes
📝 PYQs
📄 Model Papers
🎥 Resources

Select your course to continue 👇
"""

START_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎓 B.Tech",
            callback_data="cat_materials"
        )
    ],
    [
        InlineKeyboardButton(
            "📢 Updates",
            url="https://t.me/YOUR_CHANNEL"
        ),
        InlineKeyboardButton(
            "ℹ️ About",
            callback_data="about"
        )
    ]
])


@Client.on_message(filters.command("start"))
async def start(client, message):

    try:
        with open("users.json") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    user = message.from_user.id

    if user not in users:
        users.append(user)
        with open("users.json", "w") as f:
            json.dump(users, f)

    await message.reply_text(
        START_TEXT,
        reply_markup=START_BUTTONS
    )
