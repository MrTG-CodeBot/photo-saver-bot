from pyrogram import Client, filters
import re
import requests
import os
import time

@Client.on_message(filters.regex(r"^https://telegra.ph/file/"))
async def download(client, message):
 try:
    url = message.text
    response = requests.get(url, stream=True)
    if message.text.endswith('.jpg'):

        if response.status_code == 200:
            with open('image.JPEG', 'wb') as f:
                f.write(response.content)

            await message.reply_photo(photo='image.JPEG')
            os.remove('image.JPEG')
    elif message.text.endswith('.mp4'):
        if response.status_code == 200:
            with open('video.mp4', 'wb') as f:
                f.write(response.content)
            await message.reply_video(video='video.mp4')
            os.remove('video.mp4')
        else:      
            await message.reply_text('Failed to decode the telegraph link.')
    else:
        return
 except Exception as e:
        await message.reply_text(f"{e}")


@Client.on_message(filters.command("imagine"))
async def imagine(client, message):
 try:
    url = "https://api.waifu.pics/sfw/waifu"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open('image.jpg', 'wb') as f:
            f.write(response.content)

        await message.reply_photo(photo='image.jpg')
    else:
        await message.reply_text('Failed to generate image.')
 except Exception as e:
        await message.reply_text(f"{e}")
