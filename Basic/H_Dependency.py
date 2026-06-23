from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency Function
def get_current_user():
    return {
        "username": "vanshdeep",
        "role": "student"
    }

@app.get("/profile")
def profile(user=Depends(get_current_user)):

    return {
        "user": user
    }

@app.get("/dashboard")
def dashboard(user=Depends(get_current_user)):

    return {
        "message": f"Welcome {user['username']}"
    }