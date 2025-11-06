from abc import ABC, abstractmethod
from typing import List
from .entities import Product, ChatMessage

class IProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]: ...
    
    @abstractmethod
    def get_by_id(self, product_id: int) -> Product: ...

class IChatRepository(ABC):
    @abstractmethod
    def save_message(self, message: ChatMessage) -> None: ...
