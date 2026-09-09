from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Question(BaseModel):

    question: str
    language:str


@app.post("/ask")
def ask_ai(data:Question):
    return{
        "message": "Question recieved",
        "question":data.question,
        "language": data.language
    }