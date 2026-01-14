


from fastapi import HTTPException
from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User, UserCreate
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
        
    def register(self, playload: UserCreate) -> User:
        if self.repository.get_by_email(playload.email):
            raise HTTPException(status_code=400, detail="Email already exists")
        
        user = User(
            email=playload.email,
            full_name=playload.full_name,
            hashed_password=hash_password(playload.password[:72])
        )
        
        return self.repository.create(user)
    
    
    def login(self, email: str, password: str) -> str:
        user = self.repository.get_by_email(email)
        if not user or not user.verify_password(password[:72], user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        token = create_access_token({"sub": str(user.id)})
        return token