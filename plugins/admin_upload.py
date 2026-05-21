from pyrogram import Client, filters
import json
from config import ADMINS

temp = {}


@Client.on_message(
    filters.command("upload") &
    filters.user(ADMINS)
)
async def upload(_, message):

    try:
        _, category, year, branch, sem, subject = message.text.split(maxsplit=5)

        temp[message.from_user.id] = (
            category,
            year,
            branch,
            sem,
            subject
        )

        await message.reply_text(
            "📄 Now send PDF"
        )

    except:
        await message.reply_text(
            "Usage:\n/upload notes 2024 cse sem1 maths"
        )
        
@Client.on_message(
    filters.document &
    filters.user(ADMINS)
)
async def save(_, message):

    if message.from_user.id not in temp:
        return

    category, year, branch, sem, subject = temp[message.from_user.id]

    key = f"{category}_{year}_{branch}_{sem}_{subject.lower()}"

    try:
        with open("storage.json") as f:
            data = json.load(f)
    except:
        data = {}

    if key not in data:
        data[key] = []

    data[key].append({
        "id": message.document.file_id,
        "name": message.document.file_name
    })

    with open("storage.json", "w") as f:
        json.dump(data, f, indent=4)

    await message.reply_text(
        f"✅ Saved Successfully\n\nKey: {key}"
    )

@Client.on_message(
    filters.command("done") &
    filters.user(ADMINS)
)
async def done(_, message):

    if message.from_user.id in temp:

        del temp[message.from_user.id]

    await message.reply_text(
        "✅ Upload completed"
    )

@Client.on_message(
    filters.command("delete") &
    filters.user(ADMINS)
)
async def delete_file(_, message):

    try:
        _, category, year, branch, sem, subject = message.text.split(maxsplit=5)

        key = f"{category}_{year}_{branch}_{sem}_{subject.lower()}"

        with open("storage.json") as f:
            data = json.load(f)

        if key not in data:
            await message.reply_text(
                "⚠️ File not found"
            )
            return

        del data[key]

        with open("storage.json", "w") as f:
            json.dump(data, f, indent=4)

        await message.reply_text(
            f"🗑 Deleted\n\n{key}"
        )

    except:
        await message.reply_text(
            "Usage:\n/delete notes 2024 cse sem1 maths"
        )

@Client.on_message(
    filters.command("list") &
    filters.user(ADMINS)
)
async def list_files(_, message):

    try:
        with open("storage.json") as f:
            data = json.load(f)

        if not data:
            await message.reply_text(
                "📂 No files uploaded"
            )
            return

        text = "📚 Uploaded Files:\n\n"

        for key in data:
            text += f"• {key}\n"

        await message.reply_text(text)

    except:
        await message.reply_text(
            "⚠️ Error reading storage"
        )

@Client.on_message(
    filters.command("stats") &
    filters.user(ADMINS)
)
async def stats(_, message):

    try:
        with open("storage.json") as f:
            data = json.load(f)

    except:
        data = {}

    total = sum(len(v) for v in data.values())

    await message.reply_text(
        f"📊 Total resources: {total}"
    )

    await message.reply_text(
        f"📊 Total Materials: {len(data)}"
    )
