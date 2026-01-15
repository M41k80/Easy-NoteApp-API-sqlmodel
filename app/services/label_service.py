


from fastapi import HTTPException
from sqlmodel import Session

from app.models.label import Label, LabelCreate
from app.repositories.label_repository import LabelRepository


class LabelService:
    
    def __init__(self, db: Session):
        self.repository = LabelRepository(db)
        
        
    def list(self, owmer_id: int) -> list[Label]:
        return self.repository.list_by_user(owmer_id)
    
    
    def create(self, owner_id: int, payload: LabelCreate) -> Label:
        if self.repository.get_by_name(owner_id, payload.name):
            raise HTTPException(status_code=400, detail="Label already exists")
        
        return self.repository.create(owner_id, payload.name)
           
    
    
    def delete(self, owner_id: int , label_id: int) -> None:
        label = self.repository.get(label_id)
        
        if not label or label.owner_id != owner_id:
            raise HTTPException(status_code=404, detail="Label not found or not authorized")
        
        self.repository.delete(label)
        raise HTTPException(status_code=204, detail="Label deleted")
        
        