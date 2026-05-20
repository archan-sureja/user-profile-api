from schemas import UserCreate
from auth import password_hash
from db import create_session
from models import User 

class AdminUserCreate(UserCreate):
    is_admin : bool = True

first_name:str = input("Enter first name: ")
last_name:str = input("Enter last name: ")
username:str = input("Enter username(only letters , . and _): ")
password:str = input("Enter password(minimum 8 characters): ")
email:str = input("Enter email: ")
bio:str = input("Enter bio (optional): ")

admin_data = AdminUserCreate(
    first_name=first_name,
    last_name=last_name,
    username=username,
    password=password_hash.hash(password),
    email=email,
    bio=bio
)

async def create_admin():
    async with create_session() as session:
        admin = User(**admin_data.model_dump())
        session.add(admin)
        await session.commit()
        print("Admin user created successfully")

if __name__ == "__main__":
    import asyncio 
    asyncio.run(create_admin())

