from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.schemas.profile import ProfileUpdate
from app.models.user import user_collection

router = APIRouter()

@router.get("/")
async def get_profile(
    current_user=Depends(get_current_user)
):

    user = await user_collection.find_one(
        {"email": current_user["email"]}
    )

    return {
    "name": user["name"],
    "email": user["email"],
    "role": user["role"],

    "college": user.get("college", ""),

    "branch": user.get("branch", ""),
    "semester": user.get("semester", ""),
    "division": user.get("division", ""),
    "roll_number": user.get("roll_number", ""),

    "department": user.get("department", ""),
    "subjects": user.get("subjects", []),

    "designation": user.get("designation", ""),
    "experience": user.get("experience", 0),

    "bio": user.get("bio", "")
}
@router.put("/")
async def update_profile(
    profile: ProfileUpdate,
    current_user=Depends(get_current_user)
):

    await user_collection.update_one(
        {
            "email": current_user["email"]
        },
        {
            "$set": {

    "college": profile.college,

    "branch": profile.branch,
    "semester": profile.semester,
    "division": profile.division,
    "roll_number": profile.roll_number,

    "department": profile.department,
    "subjects": profile.subjects,

    "designation": profile.designation,
    "experience": profile.experience,

    "bio": profile.bio
}
        }
    )

    return {
        "message": "Profile updated successfully"
    }