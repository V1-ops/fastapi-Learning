from fastapi import FastAPI

app = FastAPI()

students = [
    "Student1",
    "Student2",
    "Student3",
    "Student4",
    "Student5",
    "Student6",
    "Student7",
    "Student8",
    "Student9",
    "Student10"
]

@app.get("/students")
def get_students(skip: int = 0,
                 limit: int = 5):

    return students[skip:skip + limit]