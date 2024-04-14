from typing import Dict, Union

from pymongo import MongoClient

from DazaiRobot import DB_NAME, MONGO_DB_URI

client = MongoClient(MONGO_DB_URI)
db = client[DB_NAME]

coupledb = db.couple


async def _get_lovers(chat_id: int):
    lovers = coupledb.find_one({"chat_id": chat_id})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers


async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    coupledb.update_one({"chat_id": chat_id}, {"$set": {"couple": lovers}}, upsert=True)

