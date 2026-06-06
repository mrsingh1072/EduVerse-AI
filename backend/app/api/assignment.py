from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.assignment_service import evaluate_assignment
from app.services.history_service import save_history
from app.dependencies.auth import get_current_user

router = APIRouter()


class AssignmentRequest(BaseModel):
    assignment: str


@router.post("/")
async def assignment_check(
    data: AssignmentRequest,
    current_user=Depends(
        get_current_user
    )
):

    result = evaluate_assignment(
        data.assignment
    )

    if "error" not in str(result).lower():

        await save_history(
            user_email=current_user["email"],
            history_type="assignment",
            question="Assignment Evaluation",
            answer=result
        )

    return {
        "evaluation": result
    }