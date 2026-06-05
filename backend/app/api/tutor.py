from fastapi import APIRouter
from pydantic import BaseModel
from app.services.tutor_service import tutor_response

router = APIRouter()

class TutorRequest(BaseModel):
    question: str

@router.post("/")
async def ai_tutor(data: TutorRequest):

    answer = tutor_response(
        data.question
    )

    return {
        "answer": answer
    }