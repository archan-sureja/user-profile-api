from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy import String, Boolean, Text, null

class Base(DeclarativeBase):
    """Base class for every model , used for metadata"""
    pass 

class User(Base):
    """ User model used to map users table from DB"""
    __tablename__ : str = "users" 
    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str] = mapped_column(String(30),nullable=False)
    last_name : Mapped[str] = mapped_column(String(30),nullable=False)
    username : Mapped[str] = mapped_column(String(30),nullable=False,unique=True)
    password : Mapped[str] = mapped_column(String(255),nullable=False)
    email : Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    is_admin : Mapped[bool] = mapped_column(Boolean,default=False)
    is_active : Mapped[bool] = mapped_column(Boolean,default=True)
    bio : Mapped[str] = mapped_column(Text,nullable=True)

