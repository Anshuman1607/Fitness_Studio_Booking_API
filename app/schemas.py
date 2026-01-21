from pydantic import BaseModel, EmailStr
from datetime import datetime

class usercreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class userlogin(BaseModel):
    email: EmailStr
    password: str


class token(BaseModel):
    access_token: str
    token_type: str


class ClassCreate(BaseModel):
    title: str
    description: str
    instructor: str
    available_slots: int


class ClassResponse(ClassCreate):
    id: int

    class Config:
        from_attributes = True

class BookingResponse(BaseModel):
    id: int
    user_id: int
    class_id: int
    booking_time: datetime

    class Config:
        from_attributes = True