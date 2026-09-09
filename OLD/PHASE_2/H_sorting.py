from fastapi import FastAPI

app = FastAPI()

students = [
    {"name": "Vanshdeep", "cgpa": 8.5},
    {"name": "Rahul", "cgpa": 7.2},
    {"name": "Aman", "cgpa": 9.1},
    {"name": "Priya", "cgpa": 8.0}
]

@app.get("/students")
def get_students():
    
    sorted_students = sorted(
        students,
        key=lambda x: x["name"]
    )

    return sorted_students