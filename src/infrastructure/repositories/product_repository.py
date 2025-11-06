from sqlalchemy.orm import Session
from src.domain.entities import Product
from src.domain.repositories import IProductRepository
from src.infrastructure.db.models import ProductORM

class ProductRepository(IProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return [Product(**vars(p)) for p in self.db.query(ProductORM).all()]

    def get_by_id(self, product_id: int):
        p = self.db.query(ProductORM).filter(ProductORM.id == product_id).first()
        return Product(**vars(p))
