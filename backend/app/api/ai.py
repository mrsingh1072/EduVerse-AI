from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.openrouter_service import generate_response
from app.services.history_service import save_history
from app.dependencies.auth import get_current_user

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def ai_chat(
    chat: ChatRequest,
    current_user=Depends(
        get_current_user
    )
):

    answer = generate_response(
        chat.message
    )

    # Save only successful responses
    if "error" not in str(answer).lower():

        await save_history(
            user_email=current_user["email"],
            history_type="chat",
            question=chat.message,
            answer=answer
        )

    return {
        "answer": answer
    }