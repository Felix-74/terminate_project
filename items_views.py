from typing import Annotated

import router as router
from fastapi import APIRouter, Path

router = APIRouter(prefix="/itemps")

@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@app.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@app.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }
