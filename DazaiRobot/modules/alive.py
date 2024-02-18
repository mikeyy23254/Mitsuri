from pyrogram import version as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import version as telever
from telethon import version as tlhver

from DazaiRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot

VIDEO  = "https://telegra.ph/file/13f087d75c66ca1759ef4.mp4"


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"Hᴇʏ Hᴏɴᴇʏ {message.from_user.mention},\n\nɪ ᴀᴍ {BOT_NAME}\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» ᴍʏ ʜᴏɴᴇʏ : [Mikey](tg://user?id={OWNER_ID})\n\n"
    TEXT += f"» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ : {telever} \n\n"
    TEXT += f"» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {tlhver} \n\n"
    TEXT += f"» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {pyrover} \n━━━━━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Ahjin_sprt"),
        ]
    ]
    await message.reply_video(
        VIDEO ,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


mod_name = "Aʟɪᴠᴇ"
