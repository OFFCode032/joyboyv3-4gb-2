import os 
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
token = os.environ.get('TOKEN','6488060321:AAHprWjPk-gPWPlrnYUAQ8JauhtxiTCD1rw')
botid = token.split(':')[0]
ADMIN = int(os.environ.get("ADMIN", "5104903730"))

from helper.database import botdata, find_one, total_user,getid

from helper.progress import humanbytes


@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["myusers"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	id = str(getid())
	ids = id.split('\n')
	try:
		await message.reply_text(f"⚡️ All IDS : {ids}\n\n⚡️ Total User :- {total_user()}\n\n⚡️ Total Renamed File :- {total_rename}\nV Total Size Renamed :- {humanbytes(int(total_size))}",quote=True,
					 reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Close Menu 🦋", callback_data="cancel")]])
					)
	except MessageTooLong:
		with open('users.txt', 'w+') as outfile:
			outfile.write(f"😁All IDS : {ids}\n\n⚡️ Total User :- {total_user()}\n\n⚡️ Total Renamed File :- {total_rename}\nV Total Size Renamed :- {humanbytes(int(total_size))}")
			await message.reply_document('users.txt', caption="Users:")
