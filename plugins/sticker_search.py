import asyncio
from pyrogram import Client, filters
import requests
from info import REQUESTED_CHANNEL

@Client.on_message(filters.command("tgsticker"))
async def google_text(client, message):
    try:
        user_query = message.text.split()[1:]
        if not user_query:
            await message.reply_text("please provide a query <code>/tgsticker gojo</code>")
        encoded_query = " ".join(user_query).replace(" ", "%20")

        response = requests.get(f"https://api.safone.dev/tgsticker?query={encoded_query}&limit=1")
        if response.status_code == 200:
            data = response.json()
            sticker = data['results'][0]
            link = sticker['link']
            await client.send_message(message.chat.id, text=f"{link}")
            await client.send_message(REQUESTED_CHANNEL, text=f"#sᴛɪᴄᴋᴇʀ_sᴇᴀʀᴄʜ\nʜᴇʏ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {user_query}")

    except Exception as e:
       await message.reply_text(f"An error occurred: {e}")
