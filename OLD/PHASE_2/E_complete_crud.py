from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ------------------------
# Pydantic Model
# ------------------------
class Student(BaseModel):
    name: str
    age: int
    course: str

# ------------------------
# Fake Database
# ------------------------
students = []

# ------------------------
# CREATE
# ------------------------
@app.post("/students")
def create_student(student: Student):

    student_data = student.model_dump()

    students.append(student_data)

    return {
        "message": "Student created successfully",
        "student": student_data
    }

# ------------------------
# READ ALL
# ------------------------
@app.get("/students")
def get_all_students():

    return {
        "total_students": len(students),
        "students": students
    }

# ------------------------
# READ ONE
# ------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

# ------------------------
# UPDATE
# ------------------------
@app.put("/students/{student_id}")
def update_student(student_id: int,
                   updated_student: Student):

    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = updated_student.model_dump()

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }

# ------------------------
# DELETE
# ------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "deleted_student": deleted_student
    }