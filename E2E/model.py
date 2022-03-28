from pydantic import BaseModel, Field


class Auth(BaseModel):
    token: str = Field(..., alies='token')
    teacher_id: str = Field(..., alies='teacher_id')
