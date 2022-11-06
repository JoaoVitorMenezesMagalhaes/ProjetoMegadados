from typing import Union

from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import crud, models, schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import uuid

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Adiciona produto no estoque
@app.post("/items/", status_code=201, response_model=schemas.Item)
def create_item(item_create: schemas.ItemCreate, db: Session = Depends(get_db)):
    print(item_create)
    item = schemas.Item()
    item.id = uuid.uuid4()
    item.name = item_create.name
    item.price = item_create.price
    item.amount = item_create.amount
    crud.create_item(db, item)
    return item

# Verifica Estoque
@app.get("/itens")
def get_estoque(db: Session = Depends(get_db)):
    return crud.get_items(db)

# Verifica um item do estoque
@app.get("/itens/{item_id}", response_model = schemas.Item)
def get_item(item_id: str, db: Session = Depends(get_db)):
    return crud.get_items_by_id(db, item_id)

#Atualiza item do estoque
@app.put("/items/{item_id}")
def update_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.update_item(db, item)

# Deleta item do estoque
@app.delete("/items/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id)
