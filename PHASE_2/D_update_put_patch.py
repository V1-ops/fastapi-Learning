from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

fake_users = {
    1: {"name": "John", "age": 30}
}

#PUT full update
class UserPut(BaseModel):
    name: str
    age: int
@app.put("/users/{user_id}")
def full_update_user(user_id:int , user:UserPut):
    fake_users[user_id]= user.model_dump()
    return{
        "message": "User updated successfully using PUT",
        "user":fake_users[user_id]
    }

    