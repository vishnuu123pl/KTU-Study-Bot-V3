from pyrogram import Client, filters
import json


@Client.on_callback_query(
    filters.regex(r"^(notes|pyq|model|video)_(.+)$")
)
async def send_resource(_, query):

    key = query.data.lower()

    try:
        with open("storage.json") as f:
            data = json.load(f)

    except:
        data = {}

    if key not in data:

        await query.answer(
            "⚠️ 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦 𝘯𝘰𝘵 𝘶𝘱𝘭𝘰𝘢𝘥𝘦𝘥 𝘺𝘦𝘵",
            show_alert=True
        )
        return

    files = data[key]

    for file in files:

        await query.message.reply_document(
            file["id"]
        )

    await query.answer()
