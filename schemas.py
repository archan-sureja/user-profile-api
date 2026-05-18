from pydantic import BaseModel, EmailStr , field_validator , Field

class UserCreate(BaseModel):
    first_name: str = Field(min_length=1,max_length=30)
    last_name : str = Field(min_length=1,max_length=30)
    username : str = Field(min_length=8,max_length=30)
    password : str = Field(min_length=8,max_length=30)
    email : EmailStr
    bio : str | None = Field()

    @field_validator("first_name","last_name","username","password","bio",mode="before")
    @classmethod 
    def strip_val(cls,val:str)->str:
        return val.strip()

    @field_validator("bio",mode="after")
    @classmethod 
    def check_empty(cls,val:str)->None:
        if not val:
            return None 
