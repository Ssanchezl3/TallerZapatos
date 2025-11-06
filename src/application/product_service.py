from typing import List
from src.domain.entities import Product
from src.domain.repositories import IProductRepository

class ProductService:
    def __init__(self, product_repo: IProductRepository):
        self.product_repo = product_repo

    def list_products(self) -> List[Product]:
        return self.product_repo.get_all()

    def get_product(self, product_id: int) -> Product:
        return self.product_repo.get_by_id(product_id)
