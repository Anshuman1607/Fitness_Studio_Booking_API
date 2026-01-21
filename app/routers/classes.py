from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.database import Engine
from app.schemas import ClassCreate, ClassResponse
from app.models import FitnessClass

router = APIRouter(
    prefix="/classes",
    tags=["classes"]
)

# Create a new fitness class
@router.post("/", response_model=ClassResponse)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_Class = FitnessClass(**class_data.model_dump())
    db.add(new_Class)
    db.commit()
    db.refresh(new_Class)
    return new_Class

# Get all fitness classes
@router.get("/", response_model=list[ClassResponse])
def get_classes(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    classes = db.query(FitnessClass).all()
    return classes

