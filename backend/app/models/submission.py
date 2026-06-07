from pydantic import BaseModel

class AssignmentSubmission(BaseModel):
    assignment_id: str
    student_email: str
    submission_text: str