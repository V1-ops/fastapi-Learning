"""
Project: Student Manager API (CRUD)
Run:
uvicorn I_student_crud:app --reload
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title = " student Manager API")

# pydantic model
class Student(BaseModel):
    name: str
    age: int
    course: str

# fake Db
STUDENT = []

@app.post("/students")
def add_student(student:Student):
    STUDENT.append(student)
    return {
        "message": "Student added succssefully",
        "student":student
    }
#Get
@app.get("/students")
def get_all_students():
    return STUDENT

#update
class StudentUpdate(BaseModel):
    age: int
    course: str

@app.put("/students/{student_name}")
def update_student(student_name: str , updated_data:StudentUpdate):
    for student in STUDENT:
        if student.name.lower() == student_name.lower():
            student.age = updated_data.age
            student.course = updated_data.course
            return {
                   "message": "Student update succssefully",
                   "student":student
            }
    return {"error": "Student not found "}    

       
@app.delete("/students/{student_name}")
def delete_students(student_name: str):
    for index, student in enumerate(STUDENT):
         if student.name.lower() == student_name.lower():
             deleted_students = STUDENT.pop(index)

             return {
                 "message": "student delete  succssefully",
                 "student":deleted_students

             }
