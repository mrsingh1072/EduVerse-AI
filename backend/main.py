from fastapi import FastAPI
from app.database.mongodb import client
from app.api.user import router as user_router
from app.api.auth import router as auth_router

app = FastAPI(
    title="EduVerse AI",
    version="1.0.0"
)

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

@app.get("/")
async def home():
    try:
        await client.admin.command("ping")
        return {
            "message": "EduVerse AI Backend Running",
            "database": "MongoDB Connected"
        }
    except Exception as e:
        return {
            "message": "MongoDB Connection Failed",
            "error": str(e)
        }
