from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

@app.get("/")
def hello_index():
    return {
        "message": "Hello my friends!",
    }

@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)