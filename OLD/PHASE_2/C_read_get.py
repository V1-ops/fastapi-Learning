from fastapi import FastAPI
app = FastAPI()
fake_users=[
    {"id":1, "name":"John"},
    {"id":2, "name":"Jane"},
]
@app.get("/users")
def get_users():
    return fake_users