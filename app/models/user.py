

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "app_user"
    id: int = Field(primary_key=True, default=None, nullable=False)
    email: str = Field(index=True, unique=True)
    full_name: str = Field(default="")
    hashed_password: str 
    
class UserCreate(SQLModel):
    email: str
    full_name: str = ""
    password : str
    
class UserRead(SQLModel):
    id: int
    email: str
    full_name: str
    model_config = {"from_attributes": True} # to use the __init__ method