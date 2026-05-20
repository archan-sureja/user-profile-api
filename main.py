from sqlalchemy.ext.asyncio import AsyncSession
from config import settings
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.exc import IntegrityError
from utils import password_hash
from schemas import UserCreate, UserRes, LoginReq, Token , AdminUserRes, UserUpdate
from models import User
from db import get_session
from auth import authenticate_user, create_access_token, get_current_active_user , check_admin 
from sqlalchemy import select 

app = FastAPI(title="User Profile API")


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserRes)
async def create_user(userCreate: UserCreate, session=Depends(get_session)) -> User:

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
                status_code=status.HTTP_409_CONFLICT, detail="username already exist"
            )
        if "users_email_key" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="email already exist"
            )
    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.get("/users/me",response_model=UserRes)
async def get_profile(token: Annotated[str, Depends(oauth2_scheme)],session:AsyncSession=Depends(get_session)):
    user = await get_current_active_user(token=token,db_session=session)
    return user 

@app.patch("/users/me",response_model=UserRes)
async def update_profile(updateData:UserUpdate,token : str = Depends(oauth2_scheme),session:AsyncSession=Depends(get_session)):
    user = await get_current_active_user(token,session)
    updateDict = updateData.model_dump(exclude_unset=True)
    if user and not updateDict:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="No data provided for update"
        )
    for k,v in updateDict.items():
        setattr(user,k,v)
    await session.commit()
    await session.refresh(user)
    return user 

@app.get("/users",response_model=list[AdminUserRes])
async def get_all_users(token: Annotated[str, Depends(oauth2_scheme)],session:AsyncSession=Depends(get_session)):
    if not check_admin(token):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN
        )
    stmt = select(User)
    users = await session.scalars(stmt)
    return users.all()

@app.delete("/users/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def deactivate_user(user_id : int,token:str=Depends(oauth2_scheme),session:AsyncSession=Depends(get_session)):
    if not check_admin(token):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
        )
    user = await session.get(User,user_id)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user.is_active = False 
    await session.commit()
    return 
    
@app.post("/token")
async def login(req: LoginReq , session: AsyncSession = Depends(get_session))->Token:
    user = await authenticate_user(req.username, req.password,session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id) , "is_admin":str(user.is_admin) }, expires_delta=access_token_expires
    )
    return Token(token=access_token)