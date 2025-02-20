from pyrogram import Client, filters 
from pyrogram.types import *
from helper.database import *
from Script import script
from helper.progress import get_size, get_time, humanbytes
import shutil, psutil
import time
StartTime = time.time()
__version__ = 1.1

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Give me a caption to set.\n\nExample:- `/set_caption File Name`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**Your Caption successfully added ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**You dont have any custom caption**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**Your caption successfully deleted ✅**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**You dont have any custom caption**")

@Client.on_callback_query(filters.regex('status'))
async def stats(client, query):
  currentTime = get_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_size(total)
  used = get_size(used)
  free = get_size(free)
  sent = get_size(psutil.net_io_counters().bytes_sent)
  recv = get_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  #botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            #f'<b>Total disk space:</b> {total}\n' \
            #f'<b>Used:</b> {used}\n' \
            #f'<b>Free:</b> {free}\n' \
            #f'<b>Upload:</b> {sent}\n' \
            #f'<b>Down:</b> {recv}\n' \
            #f'<b>CPU:</b> {cpuUsage}%\n' \
            #f'<b>RAM:</b> {memory}%\n' \
            #f'<b>Disk:</b> {disk}%'
  await query.answer(script.STATUS.format(currentTime, total, used, free, sent, recv, cpuUsage, memory, disk), show_alert=True)
          
