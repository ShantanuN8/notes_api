from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional 

class NoteBase(BaseModel):
    title: str = Field(..., max_length=200, min_length=1)
    content: str = Field(..., min_length=1)
    category: Optional[str]="General"
    tags: Optional[str]= None
    is_favorite: Optional[bool] = False
    is_archived: Optional[bool] = False
    color: str = "#FFFFFF"
class NoteCreate(NoteBase):
    pass
class NoteUpdate(NoteBase):
    title: Optional[str] = Field(None,max_length=200, min_length=1)
    content: Optional[str] = Field(None,min_length=1)
    category: Optional[str] = None
    tags: Optional[str] = None
    is_favorite: Optional[bool] = None
    is_archived: Optional[bool] = None
    color: Optional[str] = None

class Note(NoteBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    class Config:
        from_attributes=True