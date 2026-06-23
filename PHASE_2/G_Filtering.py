from fastapi import FastAPI

app = FastAPI()

students = [
    {"name": "Vanshdeep", "course": "AIML"},
    {"name": "Rahul", "course": "CSE"},
    {"name": "Aman", "course": "AIML"},
    {"name": "Priya", "course": "IT"}
]

@app.get("/students")
def get_students(course: str):

    filtered_students = []

    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    return filtered_students