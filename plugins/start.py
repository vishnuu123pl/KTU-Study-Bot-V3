from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

START_TEXT = """
🎓 <b>Welcome to KTU Study Bot</b>

Your smart study companion for KTU students.

📚 Notes
📝 Previous Year Questions
📄 Model Papers
🎥 Video Resources

📖 Semester & Branch wise access
⚡ Fast and easy navigation

Select your course below 👇
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
            "💻 Source Code",
            url="https://github.com/vishnuu123pl/KTU-Study-Bot-V3"
        )
    ],
    [
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

        try:
            with open("users.json", "w") as f:
                json.dump(users, f)

        except:
            pass

    await message.reply_photo(
        photo="file_0000000066dc7208900c1d54f651a62b",
        caption=START_TEXT,
        reply_markup=START_BUTTONS
    )
