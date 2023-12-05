from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello my friends!",
    }


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.get("/hello/")
def hello(name: str = "Igor"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
