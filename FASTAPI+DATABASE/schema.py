from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int


class UserResponse(UserCreate):
    id: int

    class config:
        orm_mode = True
   
