from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name : str
    age : int
test_db = []

@app.post("/users")
def create_user(user:User):
    test_db.append(user)
    return{"message":"User created successfully", "user": user}