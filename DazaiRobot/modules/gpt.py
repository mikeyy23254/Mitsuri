#txt

import requests
import json
from DazaiRobot import pbot as app
from pyrogram import filters

@app.on_message(filters.command("chat"))
async def _sax(app,message):
    txt =await message.reply("**Generating...**")
    if len(message.command) < 2 :
        return await txt.edit("**Give me a query too**")
    query = message.text.split("/chat")[1]
    url = "https://api.safone.me/chatgpt"
    payloads = {
         "message": query,
        "chat_mode": "assistant",
        "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
        }
    headers = {"Content-Type" : "application/json"}
    response = requests.post(url, json=payloads, headers=headers)
    results = response.json()
    await txt.edit(results["message"])

__mod_name__ = "ᴄʜᴀᴛ ɢᴘᴛ"
__help__ = """
~ /chat <*your query*>
"""
