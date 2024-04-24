from pyrogram import Client, filters
from gtts import gTTS
from DazaiRobot import pbot as app


@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('speech.mp3')
    client.send_audio(message.chat.id, 'speech.mp3')

__mod_name__ = "TTS"
__help__ = """
**» /tts** - Turn text to speech
"""