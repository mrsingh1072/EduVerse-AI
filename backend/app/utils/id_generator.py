from app.database.mongodb import db
from pymongo import ReturnDocument

async def get_next_sequence(counter_name: str):

    counter = await db.counters.find_one_and_update(
        {"_id": counter_name},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )

    return counter["seq"]