from typing import Union

from tomlkit import item

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {item_id, item}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}", status_code=status.HTTP_201_CREATED)
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return "delete item with id {id}"