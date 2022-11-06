from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base



class Item(Base):
    __tablename__ = "items"

    id = Column(String(255), primary_key=True, index=True)
    name = Column(String(255))
    price = Column(Float)
    amount = Column(String(255))
    
