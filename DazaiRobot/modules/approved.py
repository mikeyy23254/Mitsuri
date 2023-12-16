import asyncio
from DazaiRobot import pbot as Michiko
from pyrogram import filters
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import FloodWait

@Michiko.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await _.approve_chat_join_request(m.chat.id, m.from_user.id)
        await _.send(m.from_user.id, text=f"{m.from_user.mention} Bro accpet your requests")
    except FloodWait as e:
        print(f"Sleeping for {e.x + 2} seconds due to floodwaits!")
        await asyncio.sleep(e.x + 2)
        await _.approve_chat_join_request(m.chat.id, m.from_user.id)
