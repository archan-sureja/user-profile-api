import re 
from pydantic import BaseModel, EmailStr , field_validator , Field, ConfigDict

class UserCreate(BaseModel):
    """schema for user creation request validation"""
    first_name: str = Field(min_length=1,max_length=30)
    last_name : str = Field(min_length=1,max_length=30)
    username : str = Field(min_length=8,max_length=30)
    password : str = Field(min_length=8,max_length=30)
    email : EmailStr
    bio : str | None 

    @field_validator("first_name","last_name","username","password",mode="before")
    @classmethod 
    def strip_val(cls,val:str)->str:
            return val.strip()
        

    @field_validator("bio",mode="after")
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
                "Username can contain only lowercase letters (a-zA-Z), numbers (0-9), dots (.), and underscores (_)"
            )
        return val 

class UserRes(BaseModel):
    id : int 
    first_name : str 
    last_name : str 
    username : str 
    email : EmailStr 
    bio : str | None 

    model_config = ConfigDict(
        from_attributes=True
    )

class LoginReq(BaseModel):
    username : str 
    password : str 

class Token(BaseModel):
    token : str 
    type : str = "bearer"