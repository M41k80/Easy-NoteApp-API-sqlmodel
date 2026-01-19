


from typing import Optional
from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, nullable=False)
    title: str
    content : str = ""
    color: Optional[str] = None
    owner_id: int = Field(foreign_key="app_user.id", nullable=False, index=True)
    
    
# DTOs
    
class NoteCreate(SQLModel):
    title: str
    content : str = ""
    color: Optional[str] = None
    label_ids: Optional[list[int]] = None
    

class NoteUpdate(SQLModel):
    title: Optional[str] = None
    content : Optional[str] = None
    color: Optional[str] = None
    label_ids: Optional[list[int]] = None
    
    
class NoteRead(SQLModel):
    id: int
    title: str
    content : str
    color: Optional[str]
    model_config = {"from_attributes": True} # to use the __init__ method