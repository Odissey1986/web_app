from database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    count = Column(Integer, default=1)

    product = relationship("Product", back_populates="order", lazy="joined")
    