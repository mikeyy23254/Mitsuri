from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from DazaiRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot

VIDEO  = "https://te.legra.ph/file/f45343278d40b5017a206.mp4"


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"**𝙷𝙴𝚈 𝙷𝙾𝙽𝙴𝚈 {message.from_user.mention},\n\nɪ ᴀᴍ {BOT_NAME}**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ  𝙷𝙾𝙽𝙴𝚈 :** [Mikey](tg://user?id={OWNER_ID})\n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
InlineKeyboardButton("𝙼𝚢 𝚂𝚠𝚎𝚎𝚝𝚑𝚎𝚊𝚛𝚝", url=f"https://t.me/YumekoUpdate/9"),
        ]
    ]
    await message.reply_video(
        VIDEO ,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "Aʟɪᴠᴇ"
