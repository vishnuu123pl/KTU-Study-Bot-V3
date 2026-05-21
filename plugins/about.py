from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ABOUT_TEXT = """
🎓 <b>𝘒𝘛𝘜 𝘚𝘵𝘶𝘥𝘺 𝘉𝘰𝘵</b>

𝘠𝘰𝘶𝘳 𝘴𝘮𝘢𝘳𝘵 𝘤𝘰𝘮𝘱𝘢𝘯𝘪𝘰𝘯 𝘧𝘰𝘳 𝘒𝘛𝘜 𝘴𝘵𝘶𝘥𝘪𝘦𝘴.

✨ 𝘍𝘦𝘢𝘵𝘶𝘳𝘦𝘴:

📚 𝘕𝘰𝘵𝘦𝘴
📝 𝘗𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘠𝘦𝘢𝘳 𝘘𝘶𝘦𝘴𝘵𝘪𝘰𝘯𝘴
📄 𝘔𝘰𝘥𝘦𝘭 𝘗𝘢𝘱𝘦𝘳𝘴
🎥 𝘝𝘪𝘥𝘦𝘰 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴
📊 𝘈𝘥𝘮𝘪𝘯 𝘜𝘱𝘭𝘰𝘢𝘥 𝘗𝘢𝘯𝘦𝘭
🔔 𝘉𝘳𝘰𝘢𝘥𝘤𝘢𝘴𝘵 𝘚𝘺𝘴𝘵𝘦𝘮
📖 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳 & 𝘉𝘳𝘢𝘯𝘤𝘩 𝘕𝘢𝘷𝘪𝘨𝘢𝘵𝘪𝘰𝘯
⚡ 𝘍𝘢𝘴𝘵 𝘧𝘪𝘭𝘦 𝘥𝘦𝘭𝘪𝘷𝘦𝘳𝘺

👨‍💻 𝘉𝘶𝘪𝘭𝘵 𝘧𝘰𝘳 𝘒𝘛𝘜 𝘴𝘵𝘶𝘥𝘦𝘯𝘵𝘴

𝘝𝘦𝘳𝘴𝘪𝘰𝘯: 3.0
"""

ABOUT_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "📢 𝘜𝘱𝘥𝘢𝘵𝘦𝘴",
            url="https://t.me/YOUR_CHANNEL" #Your Channel name(replace)
        )
    ],
    [
        InlineKeyboardButton(
            "⬅ 𝘉𝘢𝘤𝘬",
            callback_data="back_home"
        )
    ]
])


@Client.on_callback_query(
    filters.regex("^about$")
)
async def about(_, query):

    try:

        await query.message.edit_text(
            ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS
        )

    except:

        pass

    await query.answer()
