from pydantic import BaseModel


class ProfileUpdate(BaseModel):

    college: str = ""

    branch: str = ""
    semester: str = ""
    division: str = ""
    roll_number: str = ""

    department: str = ""
    subjects: list[str] = []

    designation: str = ""
    experience: int = 0

    bio: str = ""