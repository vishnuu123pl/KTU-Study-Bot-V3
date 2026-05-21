from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA
import json

CAT_LABELS = {
    "materials": "📚 Study Materials",
    "pyq": "📝 Previous Year Questions",
    "series": "📄 Series Papers",
    "model": "📖 Model Papers",
}


@Client.on_callback_query(
    filters.regex(r"^res_(\w+)_sem(\d+)_(\d+)_(\w+)_(\d+)$")
)
async def resources(_, query):

    _, branch, sem_str, year, cat, idx_str = query.data.split("_", 5)

    sem = sem_str
    sem_no = sem.replace("sem", "")

    idx = int(idx_str)

    subjects = DATA.get(branch, {}).get(sem, [])

    if idx >= len(subjects):

        await query.answer(
            "⚠️ Subject not found",
            show_alert=True
        )
        return

    subject_name = subjects[idx]

    # Example:
    # GYMAT101 | Mathematics...
    # becomes:
    # gymat101
    subject_code = (
        subject_name.split("|")[0]
        .strip()
        .lower()
    )

    text = (
        f"📚 {subject_name}\n\n"
        f"🏫 Branch: {branch.upper()}\n"
        f"📖 Semester: {sem_no}\n"
        f"📘 Scheme: {year}\n\n"
        f"Choose resource below 👇"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📚 Notes",
                callback_data=f"notes_{year}_{branch}_sem{sem_no}_{subject_code}"
            ),

            InlineKeyboardButton(
                "📝 PYQ",
                callback_data=f"pyq_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],

        [
            InlineKeyboardButton(
                "📄 Model Papers",
                callback_data=f"model_{year}_{branch}_sem{sem_no}_{subject_code}"
            ),

            InlineKeyboardButton(
                "🎥 Videos",
                callback_data=f"video_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅ Back",
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

    await query.answer()
