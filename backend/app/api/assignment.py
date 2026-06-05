from fastapi import APIRouter
from pydantic import BaseModel
from app.services.assignment_service import evaluate_assignment

router = APIRouter()

class AssignmentRequest(BaseModel):
    assignment: str

@router.post("/")
async def assignment_check(
    data: AssignmentRequest
):

    result = evaluate_assignment(
        data.assignment
    )

    return {
        "evaluation": result
    }