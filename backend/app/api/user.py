from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def test_user():
    return {"message": "User Route Working"}