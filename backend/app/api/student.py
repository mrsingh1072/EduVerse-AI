from fastapi import APIRouter, Depends
from app.dependencies.roles import require_role

router = APIRouter()


@router.get("/dashboard")
async def student_dashboard(
    current_user=Depends(
        require_role("student")
    )
):
    return {
        "message": "Welcome Student",
        "user": current_user
    }