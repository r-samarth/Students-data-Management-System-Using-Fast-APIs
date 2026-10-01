from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name: str
    department: str
    semester: int

class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
