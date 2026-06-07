from fastapi import APIRouter, Depends
from app.dependencies.roles import require_role
from app.database.mongodb import db

router = APIRouter()


@router.get("/dashboard")
async def teacher_dashboard(
    current_user=Depends(
        require_role("teacher")
    )
):

    user = await db.users.find_one(
        {
            "email": current_user["email"]
        }
    )

    assignments_created = await db.assignments.count_documents(
        {}
    )

    submissions_received = await db.submissions.count_documents(
        {}
    )

    total_students = await db.users.count_documents(
        {
            "role": "student"
        }
    )

    return {
        "teacherName": user.get(
            "name",
            ""
        ),

        "email": user.get(
            "email",
            ""
        ),

        "department": user.get(
            "department",
            ""
        ),

        "subjects": user.get(
            "subjects",
            []
        ),

        "designation": user.get(
            "designation",
            ""
        ),

        "experience": user.get(
            "experience",
            0
        ),

        "assignmentsCreated":
        assignments_created,

        "submissionsReceived":
        submissions_received,

        "totalStudents":
        total_students
    }