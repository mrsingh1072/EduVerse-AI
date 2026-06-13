from fastapi import APIRouter
from app.schemas.auth import LoginRequest
from app.models.user import user_collection
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token

import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

router = APIRouter()


@router.post("/login")
async def login(user: LoginRequest):

    # Admin Login
    if (
        user.identifier == ADMIN_EMAIL
        and user.password == ADMIN_PASSWORD
    ):
        token = create_access_token(
            {
                "email": ADMIN_EMAIL,
                "role": "admin"
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    # Student / Teacher Login
    db_user = await user_collection.find_one(
        {
            "$or": [
                {"email": user.identifier},
                {"userId": user.identifier}
            ]
        }
    )

    if not db_user:
        return {
            "message": "Invalid User"
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