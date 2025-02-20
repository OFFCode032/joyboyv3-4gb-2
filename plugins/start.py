import os, asyncio
import pymongo
import random
import shutil, psutil, time
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, InputMediaPhoto
import humanize
from helper.progress import get_size, get_time, humanbytes
from Script import script 
from helper.database import daily as daily_ 
import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_
from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size,backpre,refer,addpre,freee,claim
from pyrogram.file_id import FileId
from helper.date import add_date ,check_expi
import datetime
from datetime import date as date_
token = os.environ.get('TOKEN','6488060321:AAHprWjPk-gPWPlrnYUAQ8JauhtxiTCD1rw')
botid = token.split(':')[0]
total, used, free = shutil.disk_usage(".")
BOT_START_TIME = time.time()

SUPPORT_GROUP = os.environ.get('SUPPORT_GROUP',"missqueenbotxchat")
CHANNEL = os.environ.get('CHANNEL',"missqueenbotx")
log_channel = int(os.environ.get("LOG_CHANNEL","-1002059717598"))
STRING = os.environ.get("STRING","")
DB_NAME = os.environ.get("DB_NAME","haroonhassan4")
DB_URL = os.environ.get("DB_URL","mongodb+srv://haroonhassan4:haroonhassan4@haroonhassan4.aidylgz.mongodb.net/?retryWrites=true&w=majority")
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/d76307e5225f35c996209.jpg")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["promo"]
def profind(id):
	return dbcol.find_one({"_id":id})


#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ."
elif 12 <= currentTime.hour < 12:
	wish = 'Gᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ.'
else:
	wish = 'Gᴏᴏᴅ ᴇᴠᴇɴɪɴɢ.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	mention = message.from_user.mention
	try:
	    id = message.text.split(' ')[1]
	except:
	    m=await message.reply_sticker("CAACAgQAAxkBAAJ2AAFlXKy5e11B5VhTg4YFfLSdZlqHbwACbg8AAuHqsVDaMQeY6CcRoh4E") 
	    await asyncio.sleep(1)
	    await m.delete()
	    await message.reply_photo(
			photo=START_PIC,
			caption=script.START_TXT.format(message.from_user.mention),
			reply_markup=InlineKeyboardMarkup([[
				InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{CHANNEL}"),
				InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"https://t.me/+XFTfRRjtdgswOTM1")
			],[
				InlineKeyboardButton("◉⁠ Hᴇʟᴘ ◉", callback_data="help"),
				InlineKeyboardButton("◉⁠ Aʙᴏᴜᴛ ◉", callback_data="about")
			],[
				InlineKeyboardButton("♨️ 𝗨𝗽𝗴𝗿𝗮𝗱𝗲 𝗧𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 ♨️", callback_data="premium")
			]]
			)
		)
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,f"Your Friend {mention} already Using Our Bot")
	            await message.reply_photo(
					photo=START_PIC,
					caption=script.START_TXT.format(message.from_user.mention),
					reply_markup=InlineKeyboardMarkup([[
						InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ" ,url=f"https://t.me/{CHANNEL}"),
						InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"https://t.me/+XFTfRRjtdgswOTM1")
					],[
						InlineKeyboardButton("◉⁠ Hᴇʟᴘ ◉", callback_data="help"),
						InlineKeyboardButton("◉⁠ Aʙᴏᴜᴛ ◉", callback_data="about")
					],[
						InlineKeyboardButton("♨️ 𝗨𝗽𝗴𝗿𝗮𝗱𝗲 𝗧𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 ♨️", callback_data="premium")
					]])
				)
	        except:
	             return
	    else:
	         await client.send_message(id,f"Congrats! You Won 10 referal point your friend {mention} starting our bot")
	         user = find_one(int(id))
	         oldpoint = user["referpoint"]
	         point = oldpoint + 10
	         refer(int(id),point)
	         await message.reply_photo(
				 photo=START_PIC,
				 caption=script.START_TXT.format(message.from_user.mention),
				 reply_markup=InlineKeyboardMarkup([[
						InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ" ,url=f"https://t.me/{CHANNEL}"),
						InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"https://t.me/+XFTfRRjtdgswOTM1")
					],[
						InlineKeyboardButton("◉⁠ Hᴇʟᴘ ◉", callback_data="help"),
						InlineKeyboardButton("◉⁠ Aʙᴏᴜᴛ ◉", callback_data="about")
					],[
						InlineKeyboardButton("♨️ 𝗨𝗽𝗴𝗿𝗮𝗱𝗲 𝗧𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 ♨️", callback_data="premium")
					]]
				 )
			 )
#========================================Callback Query============================================#
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url=f'https://t.me/{CHANNEL}'),
                InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url=f'https://t.me/+XFTfRRjtdgswOTM1')
                ],[
                InlineKeyboardButton('◉⁠ Hᴇʟᴘ ◉', callback_data='help'),
                InlineKeyboardButton('◉⁠ Aʙᴏᴜᴛ ◉', callback_data='about')
            ],[
                InlineKeyboardButton('♨️ 𝗨𝗽𝗴𝗿𝗮𝗱𝗲 𝗧𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 ♨️', callback_data='premium')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="thumb"),
		InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data="caption")
                ],[
                InlineKeyboardButton("📡 ʀᴇɴᴅᴇʀɪɴɢ ɪɴғᴏ 🛰", callback_data='status')
                ],[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "start"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data = "source")
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "start"),
                InlineKeyboardButton("✘ Cʟᴏꜱᴇ", callback_data = "cancel")
            ]])            
	)
    elif data == "premium":
	    _newus = find_one(query.from_user.id)
	    user =  _newus["usertype"]
	    limit =  _newus["uploadlimit"]
	    trail= _newus["trailclaim"]
	    await query.message.edit_text(
		    text=script.PREMIUM_TXT.format(query.from_user.mention, query.from_user.id, user, humanbytes(limit)),
		    disable_web_page_preview=True,
		    reply_markup=InlineKeyboardMarkup([[
			    InlineKeyboardButton("🎉 Cʟɪᴄᴋ Hᴇʀᴇ Tᴏ Gᴇᴛ Fʀᴇᴇ Tʀᴀɪʟ 🎉", callback_data="gettrial")
		    ],[
			    InlineKeyboardButton("ғʀᴇᴇ", callback_data="free"),
			    InlineKeyboardButton("sɪʟᴠᴇʀ", callback_data="silver")
		    ],[
			    InlineKeyboardButton("ɢᴏʟᴅᴇɴ", callback_data = "gold"),
			    InlineKeyboardButton("ᴅɪᴀᴍᴏɴᴅ", callback_data = "diamond")
		    ],[
			    InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "start")
		    ]])
	    )
    elif data == "free":
        await query.message.edit_text(
            text=script.FREE_PLAN,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🎉 Cʟɪᴄᴋ Hᴇʀᴇ Tᴏ Gᴇᴛ Fʀᴇᴇ Tʀᴀɪʟ 🎉", callback_data = "gettrial")
	    ],[
                InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data = "diamond"),
                InlineKeyboardButton("1 / 4", callback_data = "pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data = "silver")
	    ],[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)

    elif data == "silver":
        await query.message.edit_text(
            text=script.SILVER_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝖯𝖺𝗒 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇", url="https://t.me/mrx369official_support_bot")
            ],[
                InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data = "free"),
                InlineKeyboardButton("2 / 4", callback_data = "pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data = "gold")
	    ],[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)

    elif data == "gold":
        await query.message.edit_text(
            text=script.GOLDEN_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝖯𝖺𝗒 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇", url="https://t.me/mrx369official_support_bot")
            ],[
                InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data = "silver"),
                InlineKeyboardButton("3 / 4", callback_data = "pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data = "diamond")
	    ],[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)

    elif data == "diamond":
        await query.message.edit_text(
            text=script.DIAMOND_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝖯𝖺𝗒 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇", url="https://t.me/mrx369official_support_bot")
            ],[
                InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data = "gold"),
                InlineKeyboardButton("4 / 4", callback_data = "pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data = "free")
	    ],[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "premium")
	    ]])            
	)
    elif data == "thumb":
        await query.message.edit_text(
            text=script.THUMB_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "help")
            ]])            
	)
    elif data == "caption":
        await query.message.edit_text(
            text=script.CAPTION_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⛔️ Bᴀᴄᴋ", callback_data = "help")
            ]])            
	)
    elif data == "source":
        await client.edit_message_media(
		query.message.chat.id,
		query.message.id,
		InputMediaPhoto("https://graph.org/file/8527760eed44272e0d69a.png")
	)
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Contact To Developer", url = "https://t.me/sonali_sahaibot")
            ],[
                InlineKeyboardButton("✘ Cʟᴏꜱᴇ / ᴅᴇʟᴇᴛᴇ⚠️", callback_data = "cancel")
	    ]])
	)
    elif data == "gettrial":
	    _newus = find_one(query.from_user.id)
	    is_claim =  _newus["trailclaim"]
	    if is_claim == "True":
		    await query.answer(
			    text=f"🤣 ʏᴏᴜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ ғʀᴇᴇ ᴛʀɪᴀʟ ɴᴏᴡ ɴᴏ ᴍᴏʀᴇ ғʀᴇᴇ ᴛʀɪᴀʟ. ᴘʟᴇᴀsᴇ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ",
			    show_alert=True
		    )
	    else:
		    mention = query.from_user.mention
		    userid = query.from_user.id
		    uploadlimit(int(userid),107374182400)
		    usertype(int(userid),"🎊 Free Trial 😁")
		    freee(int(userid))
		    claim(int(userid),"True")
		    m=await query.message.reply_text("please wait...")
		    await asyncio.sleep(0.4)
		    await m.edit_text("👀")
		    await asyncio.sleep(0.5)
		    await m.edit_text("⚡")
		    await asyncio.sleep(0.5)
		    await m.delete()
		    await query.message.reply_text(
			    text=f"Cᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs 🎉\n Yᴏᴜʀ 2 ᴅᴀʏs Fʀᴇᴇ Tʀɪᴀʟ Pʟᴀɴ Hᴀs Bᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟ Aᴄᴛɪᴠᴀᴛᴇᴅ ✅\nYᴏᴜ Cᴀɴ Eɴᴊᴏʏ Uᴘᴛᴏ 2 ᴅᴀʏs ᴀs ᴀ ᴘʀᴇᴍɪᴜᴍ Usᴇʀ 😁",
			    disable_web_page_preview=True,
			    reply_markup=InlineKeyboardMarkup([[
				    InlineKeyboardButton("🍁 Check Your Plan 🍁", callback_data="premium")
			    ],[
				    InlineKeyboardButton("⚠️ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ⚠️", callback_data = "cancel")
			    ]])
		    )
		    await client.send_message(log_channel,f"<u>FREE TRIAL PLAN CLAIMED</u>\n\n🆔 USER ID: {userid}\n🗣️ NAME: {mention}")
    elif data == "claim":
	    _newus = find_one(query.from_user.id)
	    point =  _newus["referpoint"]
	    need = 100
	    show = need - point
	    if point < int(need):
		    await query.answer(
			    text=f"𝑌𝑜𝑢𝑟 𝑅𝑒𝑓𝑓𝑒𝑟𝑎𝑙 𝑃𝑜𝑖𝑛𝑡𝑠 :- {point}\n𝑌𝑜𝑢𝑟 𝑅𝑒𝑓𝑓𝑒𝑟𝑎𝑙 𝑃𝑜𝑖𝑛𝑡𝑠 𝐼𝑠𝑛'𝑡 𝑠𝑢𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑡 𝑇𝑜 𝐶𝑙𝑎𝑖𝑚 𝑂𝑛𝑒 𝑀𝑜𝑛𝑡ℎ 𝑃𝑟𝑒𝑚𝑖𝑢𝑚 𝑃𝑙𝑎𝑛 \n𝑌𝑜𝑢 𝑁𝑒𝑒𝑑 {show} 𝑀𝑜𝑟𝑒 𝑅𝑒𝑓𝑓𝑒𝑟𝑎𝑙 𝑃𝑜𝑖𝑛𝑡𝑠 𝑇𝑜 𝐶𝑙𝑎𝑖𝑚 𝑆𝑢𝑏𝑠𝑐𝑟𝑖𝑝𝑡𝑖𝑜𝑛",
			    show_alert=True
		    )
	    else:
		    mention = query.from_user.mention
		    userid = query.from_user.id
		    new_point = point - 100
		    uploadlimit(int(query.from_user.id),107374182400)
		    usertype(int(query.from_user.id),"One Month Plan")
		    addpre(int(query.from_user.id))
		    refer(int(query.from_user.id),new_point)
		    await query.message.reply_text(
			    text=f"Congratulations 🎉 \nYour One Month Premium Plan Successful Actived ✅",
			    disable_web_page_preview=True,
			    reply_markup=InlineKeyboardMarkup([[
				    InlineKeyboardButton("🍁 Check Your Plan 🍁", callback_data="premium")
			    ],[
				    InlineKeyboardButton("⚠️ Close ⚠️", callback_data = "cancel")
			    ]])
		    )
		    await client.send_message(log_channel,f"<u>ONE MONTH PLAN CLAIMED</u>\n\n🆔 USER ID: {userid}\n🗣️ NAME: {mention}\n Remain Point: {new_point}") 
#=======================Bot rendring stats=============================#
    elif data == "rendering_info":
        await query.answer(text=script.STATS.format(get_time(time.time() - BOT_START_TIME), psutil.cpu_percent(), psutil.virtual_memory().percent, humanbytes(total), humanbytes(used), psutil.disk_usage('/').percent, humanbytes(free)), show_alert=True)
    elif data == "points":
	    user = find_one(int(query.from_user.id))
	    point = user["referpoint"]
	    await query.answer(text=f"Yᴏᴜ Hᴀᴠᴇ :- {point} Rᴇғᴇʀᴀʟ Pᴏɪɴᴛs", show_alert=True)
#============================================================================================#
@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**You are not subscribed my channel** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Updates Channel" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("Use About cmd first /about")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("database has been Cleared click on /start")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 180
       else:
           LIMIT = 20
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"`Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}`",reply_to_message_id = message.id)
       else:
       		# Forward a single message
           		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(int(message.from_user.id),epcho)
       			used_limit(int(message.from_user.id),0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Sorry! I can't upload files that are larger than {humanbytes(limit)}. File size detected {humanbytes(file.file_size)}\nUsed Daly Limit {humanbytes(used)} If U Want to Rename Large File Upgrade Your Plan ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "premium") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daly Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            uploadlimit(int(message.from_user.id),5368709120)
       		            usertype(int(message.from_user.id),"Free")
       		            backpre(int(message.from_user.id))
       		            await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("Can't upload files bigger than 2GB ")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            uploadlimit(int(message.from_user.id),5368709120)
       		            usertype(int(message.from_user.id),"Free")
       		            backpre(int(message.from_user.id))
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
