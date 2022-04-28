from typing import List, Optional

from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    text: str
    
    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    text: str

class TodoDelete(BaseModel):
    id: int