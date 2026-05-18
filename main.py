from fastapi import FastAPI 
from schemas import UserCreate 
app = FastAPI(title="User Profile API")

@app.post("/users")
def create_user(userCreate : UserCreate):
    return userCreate 

