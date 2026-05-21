from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA
import json


CAT_LABELS = {
    "materials": "📚 𝘚𝘵𝘶𝘥𝘺 𝘔𝘢𝘵𝘦𝘳𝘪𝘢𝘭𝘴",
    "pyq": "📝 𝘗𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘠𝘦𝘢𝘳 𝘘𝘶𝘦𝘴𝘵𝘪𝘰𝘯𝘴",
    "series": "📄 𝘚𝘦𝘳𝘪𝘦𝘴 𝘗𝘢𝘱𝘦𝘳𝘴",
    "model": "📖 𝘔𝘰𝘥𝘦𝘭 𝘗𝘢𝘱𝘦𝘳𝘴",
}


@Client.on_callback_query(
    filters.regex(
        r"^res_(\w+)_sem(\d+)_(\d+)_(\w+)_(\d+)$"
    )
)
async def resources(_, query):

    try:
        await query.answer()
    except:
        pass

    _, branch, sem_str, year, cat, idx_str = query.data.split("_", 5)

    sem = sem_str
    sem_no = sem.replace("sem", "")

    idx = int(idx_str)

    subjects = DATA.get(
        branch,
        {}
    ).get(
        sem,
        []
    )

    if idx >= len(subjects):

        try:
            await query.answer(
                "⚠️ 𝘚𝘶𝘣𝘫𝘦𝘤𝘵 𝘯𝘰𝘵 𝘧𝘰𝘶𝘯𝘥",
                show_alert=True
            )
        except:
            pass

        return

    subject_name = subjects[idx]
    subject_code = subject_name.split("|")[0].strip().lower()

    text = (
        f"📚 {subject_name}\n\n"
        f"🏫 𝘉𝘳𝘢𝘯𝘤𝘩: {branch.upper()}\n"
        f"📖 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳: {sem_no}\n"
        f"📘 𝘚𝘤𝘩𝘦𝘮𝘦: {year}\n\n"
        f"𝘊𝘩𝘰𝘰𝘴𝘦 𝘳𝘦𝘴𝘰𝘶𝘳𝘤𝘦 𝘣𝘦𝘭𝘰𝘸 👇"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📚 𝘕𝘰𝘵𝘦𝘴",
                callback_data=f"notes_{year}_{branch}_sem{sem_no}_{subject_code}"
            ),
            InlineKeyboardButton(
                "📝 𝘗𝘠𝘘",
                callback_data=f"pyq_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],
        [
            InlineKeyboardButton(
                "📄 𝘔𝘰𝘥𝘦𝘭 𝘗𝘢𝘱𝘦𝘳𝘴",
                callback_data=f"model_{year}_{branch}_sem{sem_no}_{subject_code}"
            ),
            InlineKeyboardButton(
                "🎥 𝘝𝘪𝘥𝘦𝘰𝘴",
                callback_data=f"video_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅ 𝘉𝘢𝘤𝘬",
                callback_data=f"sub_{branch}_{sem}_{year}_{cat}"
            )
        ]
    ])

    try:

        await query.message.edit_text(
            text,
            reply_markup=buttons
        )

    except:
        pass
