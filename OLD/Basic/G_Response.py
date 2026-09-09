from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question : str

class Answer(BaseModel):
    answer : str
@app.post("/ask",response_model = Answer)
def ask_ai(data:Question):
    answer = f"You asked {data.question}"

    return {
        "answer": answer,
        "model": "gpt 5.4"
    }

