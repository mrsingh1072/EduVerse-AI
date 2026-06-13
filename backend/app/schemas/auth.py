from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    identifier: str
    password: str