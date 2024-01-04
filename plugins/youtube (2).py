from pyrogram import Client, filters
import yt_dlp
from yt_dlp import YoutubeDL
import requests
import re

regex = r"^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(?:watch\?v=|embed/|v/|.+\?v=)?([^&=\n%\?]{11})"

@Client.on_message(filters.regex(regex))
async def download_video(client, message):
    try:
        url = message.text

        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestvideo[height<=?720][ext=mp4]+bestaudio[ext=m4a]/best[height<=?720][ext=mp4]/best',  
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            duration = info_dict.get('duration', None)  
            thumbnail_url = info_dict.get('thumbnail', None)  

            if video_title and thumbnail_url:
                if duration > 3300:  
                    await message.reply_text("Video duration exceeds 55 minutes. Downloading videos longer than 55 minutes is not supported.")
                    return

                downloading_message = await message.reply_text(f"Downloading {video_title}...")
                try:
                    await downloading_message.delete(delay=10)
                except Exception as e:
                    print(f"Failed to delete message: {e}")

                ydl.download([url])

                duration_minutes = int(duration) // 60

                response = requests.get(thumbnail_url, stream=True)
                thumbnail_file = open("thumbnail.jpg", "wb")
                for chunk in response.iter_content(1024):
                    thumbnail_file.write(chunk)
                thumbnail_file.close()

                try:
                    await client.send_video(
                        chat_id=message.chat.id,
                        video=f"{video_title}.mp4",
                        caption=f" ᴛɪᴛʟᴇ: **{video_title}**\n⌛️ ᴅᴜʀᴀᴛɪᴏɴ: {duration_minutes} ᴍɪɴᴜᴛᴇs\n sᴜᴘᴘᴏʀᴛ: <a href='https://t.me/sd_bots'> ᴛᴇᴀᴍ sᴅ ʙᴏᴛs </a>",
                        thumb="thumbnail.jpg"
                    )
                    await message.reply_text("ᴜᴘʟᴏᴀᴅᴇᴅ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                except Exception as e:
                    print(f"Error sending video: {e}")

            else:
                await message.reply_text("ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴜʀʟ.")

    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ: {e}")