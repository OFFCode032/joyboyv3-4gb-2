import os
from pyrogram import Client, filters
from helper.date import *
from helper.database import *
ADMIN = int(os.environ.get("ADMIN", 5104903730))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002059717598"))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("One Month Plan",callback_data = "vip1"), 
        			InlineKeyboardButton("Two Month Plan",callback_data = "vip2") ],[ 
        			InlineKeyboardButton("Three Month Plan",callback_data = "vip3")],[ 
        			InlineKeyboardButton("Six Month Plan",callback_data = "vip4")]]))
        			

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"One Month Plan")
	addpre(int(user_id))
	await update.message.edit("Added successfully To One Month Plan")
	await bot.send_message(user_id,"Your One Month Plan Activated checkout Your Plan /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"Two Month Plan")
	addpre1(int(user_id))
	await update.message.edit("Added successfully Two Month Plan")
	await bot.send_message(user_id,"Hey Your Two Month Plan actived checkout your plan /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"Three Month Plan")
	addpre2(int(user_id))
	await update.message.edit("Added successfully Three Month Plan")
	await bot.send_message(user_id,"Hey Your 3 month plan activated Checkout your plan /myplan")
	
@Client.on_callback_query(filters.regex('vip4'))
async def vip4(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"Six Month Plan")
	addpre3(int(user_id))
	await update.message.edit("Added successfully To Six Month Plan")
	await bot.send_message(user_id,"Hey Your 6 month plan actived checkout your plan /myplan")

#================== Free Trail Code ==============#
@Client.on_callback_query(filters.regex('trail'))
async def trail(bot,update):
	user_id = update.from_user.id
	mention = update.from_user.mention
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"Free Trail 🎉")
	freee(int(user_id))
	claim(int(user_id),"True")
	await update.message.edit("Congratulations 🎉 \nYour Two Days Free Trail Plan Successful Actived ✅")
	await bot.send_message(LOG_CHANNEL,f"<u>FREE TRAIL CLAIMED</u>\n🆔 USER ID: {user_id}\n🗣️ NAME: {mention}")
