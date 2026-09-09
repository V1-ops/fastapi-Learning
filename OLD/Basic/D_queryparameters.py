from fastapi import FastAPI
app = FastAPI()
@app.get("/items")
def get_items(name: str):
    return {"searched for" : name}
