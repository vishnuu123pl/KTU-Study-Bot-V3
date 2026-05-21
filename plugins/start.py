from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

START_TEXT = """
🎓 <b>𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 KTU 𝘚𝘵𝘶𝘥𝘺 𝘉𝘰𝘵</b>

𝘠𝘰𝘶𝘳 𝘢𝘭𝘭-𝘪𝘯-𝘰𝘯𝘦 𝘴𝘵𝘶𝘥𝘺 𝘤𝘰𝘮𝘱𝘢𝘯𝘪𝘰𝘯 𝘧𝘰𝘳 KTU 𝘴𝘵𝘶𝘥𝘦𝘯𝘵𝘴.

╭─ ✦ 𝘈𝘷𝘢𝘪𝘭𝘢𝘣𝘭𝘦 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴 ✦ ─╮
📚 𝘕𝘰𝘵𝘦𝘴
📝 𝘗𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘠𝘦𝘢𝘳 𝘘𝘶𝘦𝘴𝘵𝘪𝘰𝘯𝘴
📄 𝘔𝘰𝘥𝘦𝘭 𝘗𝘢𝘱𝘦𝘳𝘴
🎥 𝘝𝘪𝘥𝘦𝘰 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴
╰─────────────────────╯

📖 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳 & 𝘉𝘳𝘢𝘯𝘤𝘩 𝘞𝘪𝘴𝘦 𝘈𝘤𝘤𝘦𝘴𝘴
⚡ 𝘍𝘢𝘴𝘵 • 𝘖𝘳𝘨𝘢𝘯𝘪𝘻𝘦𝘥 • 𝘌𝘢𝘴𝘺

👇 𝘚𝘦𝘭𝘦𝘤𝘵 𝘺𝘰𝘶𝘳 𝘤𝘰𝘶𝘳𝘴𝘦 𝘵𝘰 𝘨𝘦𝘵 𝘴𝘵𝘢𝘳𝘵𝘦𝘥
"""

START_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎓 𝘉.𝘛𝘦𝘤𝘩",
            callback_data="cat_materials"
        )
    ],
    [
        InlineKeyboardButton(
            "💻 𝘚𝘰𝘶𝘳𝘤𝘦 𝘊𝘰𝘥𝘦",
            url="https://github.com/vishnuu123pl/KTU-Study-Bot-V3"
        ),
        InlineKeyboardButton(
            "ℹ️ 𝘈𝘣𝘰𝘶𝘵",
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
        photo="https://pic-link-bot.lovable.app/i/telegram-1779366829596-64036ff9.jpg",
        caption=START_TEXT,
        reply_markup=START_BUTTONS
    )
