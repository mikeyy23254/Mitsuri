import os, time
import openai
from pyrogram import filters
from DazaiRobot import pbot as app
from pyrogram.enums import ChatAction, ParseMode
from gtts import gTTS



openai.api_key = "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"




@app.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&","Mitsuri "]))
async def chat(app :app, message):

    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**Hello! How can I assist you today?**")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**Error**: {e} ")        






@app.on_message(filters.command(["assis"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(app :app, message):

    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**Hello! How can I assist you today?**")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            text = x    
            tts = gTTS(text, lang='en')
            tts.save('output.mp3')
            await app.send_voice(chat_id=message.chat.id, voice='output.mp3')
            os.remove('output.mp3')            

    except Exception as e:
        await message.reply_text(f"**Error**: {e} ") 





__mod_name__ = "ᴄʜᴀᴛ ɢᴘᴛ"
__help__ = """
~ /ask <*your query*>
"""