from decimal import Decimal
from typing import List, Union
from uuid import UUID

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str = None
    price: float = None
    amount: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: Union[UUID, None] = None

    class Config:
        orm_mode = True
