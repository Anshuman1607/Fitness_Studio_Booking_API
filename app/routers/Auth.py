from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, auth
from app.dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# User signup
@router.post("/signup")
def signup(user: schemas.usercreate, db: Session = Depends(get_db)):
    exists = db.query(models.User).filter(models.User.email == user.email).first()
    if exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    NEW_USER = models.User(
        name = user.username,
        email= user.email,
        password = auth.hashpassword(user.password)
    )
    db.add(NEW_USER)
    db.commit()
    db.refresh(NEW_USER)
    return {"message": "USER CREATED SUCCESSFULLY!!"}


# User login
@router.post("/login", response_model=schemas.token)
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"user_id": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}