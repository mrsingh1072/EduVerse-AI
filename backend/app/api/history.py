from fastapi import APIRouter, Depends
from app.database.mongodb import db
from app.dependencies.auth import get_current_user

router = APIRouter()


@router.get("/")
async def get_all_history():

    history = []

    cursor = db.chat_history.find()

    async for item in cursor:
        item["_id"] = str(item["_id"])
        history.append(item)

    return history


@router.get("/me")
async def get_my_history(
    current_user=Depends(
        get_current_user
    )
):

    history = []

    cursor = db.chat_history.find(
        {
            "user_email":
            current_user["email"]
        }
    )

    async for item in cursor:
        item["_id"] = str(item["_id"])
        history.append(item)

    return history


@router.delete("/")
async def delete_my_history(
    current_user=Depends(
        get_current_user
    )
):

    result = await db.chat_history.delete_many(
        {
            "user_email":
            current_user["email"]
        }
    )

    return {
        "deleted_records":
        result.deleted_count
    }