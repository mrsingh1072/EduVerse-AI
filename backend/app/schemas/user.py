from typing import Optional
from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    role: str = "student"

    # Student Fields
    studentType: Optional[str] = None

    schoolName: Optional[str] = None
    studentClass: Optional[str] = None

    collegeName: Optional[str] = None
    degree: Optional[str] = None
    course: Optional[str] = None
    yearSemester: Optional[str] = None

    # Teacher Fields
    subject: Optional[str] = None
    qualification: Optional[str] = None
    experience: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str