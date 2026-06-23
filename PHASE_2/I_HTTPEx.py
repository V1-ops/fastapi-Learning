from fastapi import FastAPI, HTTPException

app = FastAPI()

students = [
    {"name": "Vanshdeep"},
    {"name": "Rahul"}
]

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]