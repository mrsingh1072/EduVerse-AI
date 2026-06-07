from fastapi import APIRouter
from app.database.mongodb import db
from app.models.submission import AssignmentSubmission

router = APIRouter()

@router.post("/")
async def submit_assignment(
    data: AssignmentSubmission
):

    result = await db.submissions.insert_one(
        data.dict()
    )

    return {
        "message": "Assignment submitted successfully",
        "submission_id": str(result.inserted_id)
    }