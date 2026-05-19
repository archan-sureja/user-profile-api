from fastapi import FastAPI, Depends , status, HTTPException
from sqlalchemy.exc import IntegrityError 
from utils import password_hash 
from schemas import UserCreate, UserCreateRes
from models import User 
from db import get_session  
app = FastAPI(title="User Profile API")

@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=UserCreateRes)
async def create_user(userCreate : UserCreate , session = Depends(get_session))->User:

    raw_password = userCreate.password 
    hashed_password = password_hash.hash(raw_password) 
    userCreate.password = hashed_password 

    user = User(**userCreate.model_dump())

    try:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    except IntegrityError as e:
        await session.rollback()
        if "users_username_key" in str(e.orig):
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail= "username already exist"

            )
        if "users_email_key" in str(e.orig):
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail="email already exist"
            )
    return user


    
