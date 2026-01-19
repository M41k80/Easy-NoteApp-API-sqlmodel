from typing import Iterator
from sqlmodel import SQLModel, Session, create_engine
import os

from app.core.config import settings


raw_url = os.environ["DATABASE_URL"]

url = raw_url

if url.startswith("postgres://"):
    url = "postgresql+psycopg://" + url[len("postgres://"):]
elif url.startswith("postgresql://") and "+psycopg" not in url:
    url = "postgresql+psycopg://" + url[len("postgresql://"):]
    
    
    
    
engine = create_engine(
    url,
    pool_pre_ping=True,
)


# engine = create_engine(
# 	settings.DATABASE_URL,
# 	echo=False,
# 	connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
# ) just in development

def init_db() -> None:
    if settings.ENVIRONMENT == "DEVELOPMENT":
        SQLModel.metadata.create_all(engine)
    # SQLModel.metadata.create_all(engine)  #development
    
    
def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
        
        
        