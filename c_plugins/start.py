from pyrogram import enums, filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from info import DATABASE_URI, DATABASE_NAME
from pymongo import MongoClient

client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]
collection = db["clone_bots"]

@Client.on_message(filters.command("start"))
async def start(client, message: Message):
    button = [[ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/sd_bots"),
                ],[
                InlineKeyboardButton("ʜᴇʟᴘ" , callback_data='help') ,
                InlineKeyboardButton("ᴀʙᴏᴜᴛ" , callback_data='about')
            ]]
    await message.reply_text(f"**__ʜɪ {message.from_user.mention}__**\n**__ᴄʟɪᴄᴋ ʜᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʙᴜᴛᴛᴏɴs__**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_message(filters.command("help"))
async def start(client, message: Message):
    buttons = [[
         InlineKeyboardButton('ɢᴏᴏɢʟᴇ ᴀɪ', callback_data='google'),
         ],[
         InlineKeyboardButton('sᴏɴɢ', callback_data='song'),
         InlineKeyboardButton('ɪɴsᴛᴀ', callback_data='insta'),
         InlineKeyboardButton('ᴠɪᴅᴇᴏ ᴛᴏ ᴀᴜᴅɪᴏ', callback_data='convert')
         ],[
         InlineKeyboardButton('ᴅᴏɴᴀᴛᴇ', callback_data='donate')
         ],[
         InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
         InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ]]
    await message.reply_text("ᴛʜᴇsᴇ ᴀʀᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴs", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
  
@Client.on_callback_query()
async def callback_handle(client, query):
    if query.data == 'start':
        buttons = [[ 
         InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/sd_bots"),
        ],[
        InlineKeyboardButton("ʜᴇʟᴘ" , callback_data='help') ,
        InlineKeyboardButton("ᴀʙᴏᴜᴛ" , callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(f"Hello {query.from_user.mention}",
                                       reply_markup=reply_markup,
                                       parse_mode=enums.ParseMode.HTML)
        
    elif query.data == 'help':
        buttons = [[
         InlineKeyboardButton('ɢᴏᴏɢʟᴇ ᴀɪ', callback_data='google'),
         ],[
         InlineKeyboardButton('sᴏɴɢ', callback_data='song'),
         InlineKeyboardButton('ɪɴsᴛᴀ', callback_data='insta'),
         InlineKeyboardButton('ᴠɪᴅᴇᴏ ᴛᴏ ᴀᴜᴅɪᴏ', callback_data='convert')
         ],[
         InlineKeyboardButton('ᴅᴏɴᴀᴛᴇ', callback_data='donate')
         ],[
         InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
         InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text("ᴛʜᴇsᴇ ᴀʀᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴs", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'google':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text("/ai {ᴜʀ ǫᴜᴇsᴛɪᴏɴ}", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'song':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text("/song {song_name} .ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ᴏʀ ᴜsᴇ /song {ʏᴛ_ʟɪɴᴋ} ᴏʀ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ʏᴛ ʟɪɴᴋ", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'insta':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text("sᴇɴᴅ ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ,sᴛᴏʀɪᴇs ᴀɴᴅ ᴘᴏsᴛ ʟɪɴᴋ ᴛᴏ ᴛʜɪs ʙᴏᴛ, ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ, ᴘᴜʙʟɪᴄ ᴏɴʟʏ", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'donate':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(f"ʜᴇʏ {query.from_user.mention}\nᴅᴏɴᴀᴛᴇ ɪғ ʏᴏᴜ ᴄᴀɴ, ᴜᴘɪ ɪᴅ:- <code>zenistu@ibl</code>", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)

    elif query.data == 'convert':
        buttons = buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='next')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(f"ʜᴇʏ {query.from_user.mention}\nɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ᴀᴜᴅɪᴏ.\nᴊᴜsᴛ sᴇɴᴅ ᴀ ᴠɪᴅᴇᴏ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ sᴇɴᴅ /ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴛʜᴇ ᴠɪᴅᴇᴏ.sᴜᴘᴘᴏᴛ ᴏɴʟʏ ᴠɪᴅᴇᴏ", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
        
   
    elif query.data == 'about':
        bot_infos = collection.find({}) 
        for bot_info in bot_infos:
            user_finame = bot_info.get("user_fname", "N/A")
            user_id = bot_info.get("user_id", "N/A")
            username = bot_info.get("username", "N/A")
        buttons = buttons = [[
            InlineKeyboardButton('Home', callback_data='start'),
            InlineKeyboardButton('close', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(f"✯ ᴏᴡɴᴇʀ: <a href='tg://user?id={user_id}'><b>{user_finame}</b></a>\n✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>\n✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>\n\n✯ ᴄʟᴏɴᴇᴅ ʙʏ: @mrtgcoderbot", reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)
    
    elif query.data == 'close':
        await query.message.delete()
        edited_keyboard = InlineKeyboardMarkup([])
        await query.answer()
        await query.message.edit_reply_markup(edited_keyboard)
