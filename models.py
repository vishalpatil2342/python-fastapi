from pydantic import BaseModel,Field
from typing import Optional

class User(BaseModel):
    id:Optional[str] = Field(default=None)
    username:str = Field(default=None)
    email:str = Field(default=None)
