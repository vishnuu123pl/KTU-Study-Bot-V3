from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BRANCHES = [
    ("💻 CSE","cse"),
    ("📡 ECE","ece"),
    ("⚡ EEE","eee"),
    ("🔬 ICE", "ice"),
    ("🔧 ME","me"),
    ("🏗 Civil","civil")
]


@Client.on_callback_query(
    filters.regex(r"^sem(\d+)_(\d+)_(\w+)$")
)
async def branch(_, query):

    sem_no, year, cat = query.matches[0].groups()

    rows=[]

    for name, code in BRANCHES:

        rows.append([
            InlineKeyboardButton(
                name,
                callback_data=f"sub_{code}_sem{sem_no}_{year}_{cat}"
            )
        ])

    rows.append([
        InlineKeyboardButton(
            "⬅ Back",
            callback_data="back_home"
        )
    ])

    try:

        await query.message.edit_text(
            f"📘 Semester {sem_no}\n\nSelect Branch 👇",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass

    await query.answer()
