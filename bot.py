import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6488060321:AAHprWjPk-gPWPlrnYUAQ8JauhtxiTCD1rw")

API_ID = int(os.environ.get("API_ID", "19580422"))

API_HASH = os.environ.get("API_HASH", "0ea3c25451bfba7c5b69895e3a454463")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
