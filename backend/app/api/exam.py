from fastapi import APIRouter
from pydantic import BaseModel
from app.services.exam_service import generate_exam

router = APIRouter()

class ExamRequest(BaseModel):
    subject: str
    difficulty: str
    questions: int

@router.post("/")
async def exam(data: ExamRequest):

    paper = generate_exam(
        data.subject,
        data.difficulty,
        data.questions
    )

    return {
        "exam": paper
    }