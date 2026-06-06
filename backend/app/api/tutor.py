from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.tutor_service import tutor_response
from app.services.history_service import save_history
from app.dependencies.auth import get_current_user

router = APIRouter()


class TutorRequest(BaseModel):
    question: str


@router.post("/")
async def ai_tutor(
    data: TutorRequest,
    current_user=Depends(
        get_current_user
    )
):

    answer = tutor_response(
        data.question
    )

    if "error" not in str(answer).lower():

        await save_history(
            user_email=current_user["email"],
            history_type="tutor",
            question=data.question,
            answer=answer
        )

    return {
        "answer": answer
    }