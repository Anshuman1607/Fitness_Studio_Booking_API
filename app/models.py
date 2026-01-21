from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database import base

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

class FitnessClass(base):
    __tablename__ = "fitness_classes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    instructor = Column(String)
    available_slots = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

class Booking(base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    class_id = Column(Integer)
    booking_time = Column(DateTime, default=datetime.now(timezone.utc))