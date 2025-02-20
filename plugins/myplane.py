import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from helper.database import  find_one,used_limit 
from helper.database import daily as daily_ 
import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_
from helper.progress import humanbytes
from helper.database import daily as daily_
from helper.date import check_expi
from helper.database import uploadlimit , usertype, backpre

@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client,message):
	used_ = find_one(message.from_user.id)	
	daily = used_["daily"]
	expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
	if expi != 0:
	     today = date_.today()
	     pattern = '%Y-%m-%d'
	     epcho = int(time.mktime(time.strptime(str(today), pattern)))
	     daily_(message.from_user.id,epcho)
	     used_limit(message.from_user.id,0)
	_newus = find_one(message.from_user.id)
	used = _newus["used_limit"]
	limit = _newus["uploadlimit"]
	remain = int(limit)- int(used)
	user =  _newus["usertype"]
	ends = _newus["prexdate"]
	if ends:
	    pre_check = check_expi(ends)
	    if pre_check == False:
	        uploadlimit(int(message.from_user.id),2147483648)
	        usertype(int(message.from_user.id),"Free")
	        backpre(int(message.from_user.id))
	if ends == None:
	    text = f"<b>User ID:- `{message.from_user.id}`\n🏷 Plan - {user}\n\n✓ Upload 2Gb Files\n✓ Daly Upload Limit - {humanbytes(limit)}\n✓ Today Used - {humanbytes(used)}\n✓ Remain - {humanbytes(remain)}\n✓ Time Out - 5 Minutes\n✓ Time Gape - Yes\n\n⏰ Validity - Lifetime</b>"
	else:
	    normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
	    txt = f"User ID:- {message.from_user.id}\nPlan :- {user}\nDaly Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}\n\nYour Plan Ends On :- {normal_date}"
	    
	if user == "Free":
	    await message.reply(text,quote = True,reply_markup = InlineKeyboardMarkup([[       			InlineKeyboardButton("Upgrade 💰💳",callback_data = "premium"), InlineKeyboardButton("Cancel ✖️ ",callback_data = "cancel") ]]))
	else:
	    await message.reply(txt,quote=True)
