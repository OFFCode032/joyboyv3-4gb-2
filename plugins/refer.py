import os
import time
from pyrogram import Client, filters, enums
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from helper.database import find_one, insert
bot_username = os.environ.get("BOT_USERNAME","renamer_4gb_fast_ibot")
start_time = time.time()

async def get_bot_uptime():
    # Calculate the uptime in seconds
    uptime_seconds = int(time.time() - start_time)
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_weeks = uptime_days // 7
    ###############################
    uptime_string = f"{uptime_days % 7} Day | {uptime_hours % 24} Hour | {uptime_minutes % 60} Min | {uptime_seconds % 60} Sec"
    return uptime_string


#===================================refer command=====================================#
@Client.on_message(filters.command("refer") & filters.private)
async def refer(client, message):
        user = find_one(int(message.from_user.id))
        points = user["referpoint"]
        buttons = [[
            InlineKeyboardButton('invite link', url=f"https://telegram.me/share/url?url=https://t.me/{bot_username}?start={message.from_user.id}&text=Hello%21%20My%20Dear%20Best%20Friend%20I%20am%20Using%20One%20of%20The%20Best%20Rename%20Bot"),
            InlineKeyboardButton(f'{points} ⏳', callback_data='points')
            ],[
            InlineKeyboardButton('🎁 ᴄʟᴀɪᴍ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ 🎁', callback_data='claim')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo="https://graph.org/file/9451179a94147933b078f.jpg",
            caption=f"Hᴇʀᴇ ɪs ʏᴏᴜʀ ʀᴇғғᴇʀᴀʟ ʟɪɴᴋ\n\nhttps://t.me/{bot_username}?start={message.from_user.id}\n\nShare this link with your friends, Each time they join, You will get 10 refferal points and after 100 points you will get 1 months Premium subscription.",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return

@Client.on_message(filters.command("ping") & filters.private) 
async def ping(client, message):
    start_t = time.time()
    rm = await message.reply_text("⛈")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = await get_bot_uptime()
    await rm.edit(f"🏓 ᴘɪɴɢ: <code>{time_taken_s:.3f} ms</code>\n\n⏰ ᴜᴘᴛɪᴍᴇ: <code>{uptime}</code>")
