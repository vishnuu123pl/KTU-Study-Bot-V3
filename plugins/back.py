from pyrogram import Client, filters
from plugins.start import START_TEXT, START_BUTTONS


@Client.on_callback_query(
    filters.regex("^back_home$")
)
async def back_home(_, query):

    try:

        await query.message.edit_text(
            START_TEXT,
            reply_markup=START_BUTTONS
        )

    except:
        pass

    await query.answer()
