from database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    count = Column(Integer, default=0)

    order = relationship("Order", back_populates="product")