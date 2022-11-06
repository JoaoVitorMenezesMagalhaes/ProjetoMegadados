from sqlalchemy.orm import Session

import models, schemas

def get_items(db: Session, limit: int = None):
    return db.query(models.Item).limit(limit).all()

def get_items_by_id(db: Session, id: str):
    return db.query(models.Item).filter(models.Item.id == id).first()

def create_item(db: Session, item: schemas.Item):
    db_item = models.Item(id = str(item.id), name = item.name, price = item.price, amount = item.amount)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: schemas.Item):
    db_item = db.query(models.Item).filter(models.Item.id == item.id).update({"name": item.name, "price": item.price, "amount": item.amount})
    db.commit()
    return db_item

def delete_item(db: Session, id: str):
    db_item = db.query(models.Item).filter(models.Item.id == id).delete()
    db.commit()
    return db_item