from DazaiRobot.modules.mongo import *
from async_pymongo import AsyncClient
from DazaiRobot import MONGO_DB_URI 

 client = AsyncClient(MONGO_DB_URI)
dbnaam = client["Levi"]

coupledb = dbname["couples"] 

async def _get_lovers(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers

async def _get_image(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["img"]
    else:
        lovers = {}
    return lovers

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(cid: int, date: str, couple: dict, img: str):
    lovers = await _get_lovers(cid)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": lovers, "img": img}},
        upsert=True,
    )