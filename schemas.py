from typing import Annotated, Literal
import re 
from pydantic import BaseModel, EmailStr , field_validator , Field, ConfigDict

NameStr= Annotated[str,Field(min_length=1,max_length=30)]
UsernameStr = Annotated[str,Field(min_length=8,max_length=30)]
PasswordStr= Annotated[str,Field(min_length=8,max_length=256)]
BioStr = Annotated[str|None, Field(max_length=500)]

class UserBase(BaseModel):
    """Base User Schema"""
    first_name: NameStr | None = None 
    last_name : NameStr | None = None 
    username : UsernameStr | None = None 
    bio : BioStr | None = None 
    email : EmailStr | None = None 

    @field_validator("first_name","last_name","username","email",mode="before")
    @classmethod 
    def strip_val(cls,val:str | None)->str:
            if val is None:
                raise ValueError("Null value not allowed")
            return val.strip()

    @field_validator("bio",mode="before")
    @classmethod 
    def check_empty_bio(cls,val:str | None)->str|None:
        if val is None:
            return val 
        elif val.strip() == "":
            return None
        return val 

    @field_validator("first_name","last_name")
    @classmethod 
    def validate_names(cls,val:str)->str:
        if not val.isalpha():
            raise ValueError("Must contain only alphabets")
        return val 
    
    @field_validator("username")
    @classmethod 
    def validate_username(cls,val:str)->str: 
        if not re.fullmatch(r"[a-zA-Z0-9_.]+",val):
            raise ValueError(
                "Username can contain only letters (a-zA-Z), numbers (0-9), dots (.), and underscores (_)"
            )
        return val

class UserCreate(UserBase):
    """schema for user creation request validation"""
    first_name: NameStr 
    last_name : NameStr
    username : UsernameStr 
    password : PasswordStr
    email : EmailStr 
    bio : BioStr | None 

class UserUpdate(UserBase):
    pass 

class UserRes(UserBase):
    id : int

    model_config = ConfigDict(
        from_attributes=True
    )

class AdminUserRes(UserRes):
    is_active : bool 
    is_admin : bool

class LoginReq(BaseModel):
    username : str 
    password : str 

class Token(BaseModel):
    token : str 
    type : Literal["bearer"] = "bearer"