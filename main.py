import uvicorn
from fastapi import FastAPI,Body
from pydantic import BaseModel, EmailStr

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {
        "message": "Hello my friends!",
    }


@app.post("/users/")
def create_user(email: EmailStr=Body()):
    return {
        "message": "success",
        "email": email,
    }

@app.get("/hello/")
def hello(name: str = "Igor"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}
@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}

@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]

@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id": item_id,
        },
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
