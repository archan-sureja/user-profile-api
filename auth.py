from config import settings
import jwt
from datetime import timedelta, datetime, timezone
from utils import password_hash
from sqlalchemy import select
from models import User
from fastapi  import HTTPException , status
from sqlalchemy.ext.asyncio import AsyncSession

async def authenticate_user(username,password,db_session: AsyncSession)->User|None:
    stmt = select(User).where(User.username==username)
    user = await db_session.scalar(stmt)
    if user and password_hash.verify(password,user.password) and user.is_active:
        return user 
    return None 
    

def create_access_token(data : dict , expires_delta : timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(payload=to_encode,key=settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    return encoded_jwt 

async def get_current_active_user(token,db_session:AsyncSession)-> User|None:
    try:
        payload = jwt.decode(token,key=settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
    user_id = payload.get("sub")
    user = await db_session.get(User,int(user_id))  # ty:ignore[invalid-argument-type]
    if user and not user.is_active:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail="Inactive account"
        )
    return user

def check_admin(token)->bool:
    try:
        payload = jwt.decode(token,key=settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
    is_admin = payload.get("is_admin")
    return is_admin == "True"
