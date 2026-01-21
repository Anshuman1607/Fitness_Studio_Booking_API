from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import LocalSession
from app import auth, models
from app.config import Secret_key, Algorithm

OAUTH2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Get database session
def get_db():
    DB = LocalSession()
    try:
        yield DB
    finally:
        DB.close()

# Get current authenticated user
def get_current_user(db: Session = Depends(get_db), token: str = Depends(OAUTH2_scheme)):
    Payload = auth.decode_token(token)
    if Payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    user_id = Payload.get("user_id")

    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user