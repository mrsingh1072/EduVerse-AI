from fastapi import APIRouter
from app.schemas.auth import LoginRequest
from app.models.user import user_collection
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")
async def login(user: LoginRequest):

    db_user = await user_collection.find_one(
        {"email": user.email}
    )

    if not db_user:
        return {
            "message": "Invalid Email"
        }

    if not verify_password(
        user.password,
        db_user["password"]
    ):
        return {
            "message": "Invalid Password"
        }

    token = create_access_token(
        {
            "email": db_user["email"],
            "role": db_user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }