from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import Booking, FitnessClass
from app.dependencies import get_db, get_current_user
from app.schemas import BookingResponse


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

# creating booking for a class
@router.post("/{class_id}")
def create_booking(class_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found") # check if class exists
    

    booked_count = db.query(Booking).filter(Booking.class_id == class_id).count()
    if booked_count >= fitness_class.available_slots:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Class is fully booked") # check if class is fully booked
    

    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No available slots") # check available slots
    

    existing_booking = db.query(Booking).filter(Booking.user_id == current_user.id, Booking.class_id == class_id).first()
    if existing_booking:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Booking already exists for this class") # check for existing booking
    

    new_booking = Booking(
        user_id=current_user.id,
        class_id=class_id
    )
    fitness_class.available_slots -= 1
    
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    
    return {"message": "Booking created successfully", "booking_id": new_booking.id}

# getting all bookings for the current user
@router.get("/", response_model=list[BookingResponse])
def get_bookings(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    bookings = db.query(Booking).filter(Booking.user_id == current_user.id).all()
    return bookings