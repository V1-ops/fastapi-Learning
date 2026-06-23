from fastapi import FastAPI
app = FastAPI()
# static route
@app.get("/hello/world")
def static_route():
    return {"message": "This is a static route"}

# dynamic route with path parameter
@app.get("/hello/{name}")
def dynamic_route(name: str):
    return {"message": f"Hello {name} this is a dynamic route"}