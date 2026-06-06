from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.notes_service import generate_notes
from app.services.history_service import save_history
from app.dependencies.auth import get_current_user

router = APIRouter()


class NotesRequest(BaseModel):
    topic: str


@router.post("/")
async def notes(
    data: NotesRequest,
    current_user=Depends(
        get_current_user
    )
):

    notes = generate_notes(
        data.topic
    )

    if "error" not in str(notes).lower():

        await save_history(
            user_email=current_user["email"],
            history_type="notes",
            question=data.topic,
            answer=notes
        )

    return {
        "notes": notes
    }