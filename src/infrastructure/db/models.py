from sqlalchemy import Column, Integer, String, Float
from src.infrastructure.db.database import Base

class ProductORM(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    size = Column(Integer, nullable=False)
    description = Column(String)
    image_url = Column(String)
