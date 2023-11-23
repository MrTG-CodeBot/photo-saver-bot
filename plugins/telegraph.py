import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from utils import get_file_id

@Client.on_message(filters.command("telegraph"))
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("Rᴇᴘʟʏ Tᴏ A Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ 15ᴍʙ")
    file_info = get_file_id(replied)
    if not file_info:
        return await update.reply_text("Not Supported!")
    text = await update.reply_text(text="<code>Downloading To My Server ...</code>", disable_web_page_preview=True)
    media = await update.reply_to_message.download()
    await text.edit_text(text="<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>", disable_web_page_preview=True)
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)
        return
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return
    await text.edit_text(
        text=f"<b>Link :-</b>\nhttps://graph.org{response[0]}",
        disable_web_page_preview=True,
        )
