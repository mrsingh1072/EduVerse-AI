from fastapi import APIRouter, Depends
from app.dependencies.roles import require_role
from app.database.mongodb import db

router = APIRouter()


@router.get("/dashboard")
async def student_dashboard(
    current_user=Depends(
        require_role("student")
    )
):

    user = await db.users.find_one(
        {
            "email": current_user["email"]
        }
    )

    email = current_user["email"]

    assignments_submitted = await db.submissions.count_documents(
        {
            "student_email": email
        }
    )

    notes_generated = await db.chat_history.count_documents(
        {
            "user_email": email,
            "type": "notes"
        }
    )

    exams_generated = await db.chat_history.count_documents(
        {
            "user_email": email,
            "type": "exam"
        }
    )

    total_activities = await db.chat_history.count_documents(
        {
            "user_email": email
        }
    )

    return {
        "studentName": user.get("name", ""),
        "email": user.get("email", ""),

        "branch": user.get("branch", ""),
        "semester": user.get("semester", ""),

        "assignmentsSubmitted": assignments_submitted,
        "notesGenerated": notes_generated,
        "examsGenerated": exams_generated,
        "totalActivities": total_activities
    }