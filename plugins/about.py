import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6488060321:AAHprWjPk-gPWPlrnYUAQ8JauhtxiTCD1rw')
botid = token.split(':')[0]
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/d76307e5225f35c996209.jpg")
from helper.database import botdata, find_one, total_user
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	buttons = [[
		InlineKeyboardButton('《 Back To Home', callback_data='start')
	]]
	reply_markup = InlineKeyboardMarkup(buttons)
	await message.reply_photo(
		photo=START_PIC,
		caption=f"<b>◈ Name:-𝟺ɢʙ Rᴇɴᴀᴍᴇʀ Bᴏᴛ V3\n◈ Creater :-[Sᴏɴᴀʟɪ Sᴀʜᴀ](https://t.me/sonali_sahaibot)\n◈ Language :-Python3\n◈ Library :- Pyrogram 2.0\n◈ Server :- Unknown\n◈ Total Renamed File :-{total_rename}\n◈ Total Size Renamed :- {humanbytes(int(total_size))}</b>",
		reply_markup=reply_markup
	)
