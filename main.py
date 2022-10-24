from typing import Union

from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

stock = [{'name' : "arroz", 'price': 10.00, 'amount' : "13 pacotes disponíveis"},
         {'name' : "feijao", 'price': 15.00, 'amount' : "13 pacotes disponíveis"},
         {'name' : "água", 'price': 2.50, 'amount' : "45 garrafas" },
         {'name' : "refrigerante", 'price': 3.50, 'amount' : "32 latas"},
         {'name' : "carne", 'price': 35.00, 'amount' : "5 kgs disponíveis" },
]

class Item(BaseModel):
    name: str
    price: float
    amount : str

# Adiciona produto no estoque
@app.post("/items/", status_code=201, response_model=Item)
async def create_item(item_id: int, item: Item):
    item = item.dict()
    stock.append(item)
    return item

# Verifica Estoque
@app.get("/itens")
async def get_estoque():
    return stock

# Verifica um item do estoque
@app.get("/itens/{item_id}", response_model = Item)
def get_item(item_id: int):
    item = stock[item_id]
    return item

#Atualiza item do estoque
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    stock[item_id] = item
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price, "item_amount": item.amount}

# Deleta item do estoque
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item = stock[item_id]
    stock.pop(item_id)
    return {'Delete produto': item}