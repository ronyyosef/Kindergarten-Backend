from typing import TypedDict

from pydantic import BaseModel, Field

BASE_API_URL = 'https://api.kindergartenil.com'


class Auth(BaseModel):
    token: str = Field(..., alies='token')
    teacher_id: str = Field(..., alies='teacher_id')
