from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.exam_service import generate_exam
from app.services.history_service import save_history
from app.dependencies.auth import get_current_user

router = APIRouter()


class ExamRequest(BaseModel):
    subject: str
    difficulty: str
    questions: int


@router.post("/")
async def exam(
    data: ExamRequest,
    current_user=Depends(
        get_current_user
    )
):

    paper = generate_exam(
        data.subject,
        data.difficulty,
        data.questions
    )

    if "error" not in str(paper).lower():

        await save_history(
            user_email=current_user["email"],
            history_type="exam",
            question=f"{data.subject} - {data.difficulty}",
            answer=paper
        )

    return {
        "exam": paper
    }