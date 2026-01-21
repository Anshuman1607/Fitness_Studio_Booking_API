from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from app.config import Secret_key, Algorithm, Access_token_expire_minutes

pd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashing and Verifying Passwords
def hashpassword(password: str):
    password = password.encode("utf-8")[:72]
    return pd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pd_context.verify(plain_password, hashed_password)

# Creating Access Tokens
def create_access_token(data: dict, expires_delta=None):
    to_be_encoded = data.copy()
    Expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=Access_token_expire_minutes))
    to_be_encoded.update({"exp": Expire})
    return jwt.encode(to_be_encoded, Secret_key, algorithm=Algorithm)

# Decoding Access Tokens
def decode_token(token: str):
    try:
        Payload = jwt.decode(token, Secret_key, algorithms=[Algorithm])
        return Payload
    except jwt.JWTError:
        return None