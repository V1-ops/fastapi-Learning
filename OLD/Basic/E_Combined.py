from fastapi import FastAPI
app = FastAPI()

#static route
@app.get("/")
def home():
    return {"message": "Welcome to my api"}

@app.get("/about")

def about():
    return {"info":"This Api is built using FastAPI"}
#Dynamic Route (Path parameter)
@app.get("/users/{user_id}")

def get_user(user_id: int):
    return{
        "user_id":user_id,
        "message":f"Details of User{user_id}"
    }
# Multiple Path Parameters
@app.get("/users/{user_id}/orders/{order_id}")
def get_order(user_id: int, order_id: int):
    return {
        "user_id": user_id,
        "order_id": order_id
    }
# Query Parameters
@app.get("/products")
def get_products(category: str, limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }

# Path + Query Parameters Together
@app.get("/students/{student_id}")
def get_student(student_id: int, semester: int = 1):
    return {
        "student_id": student_id,
        "semester": semester
    }