from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Product:
    id: int
    name: str
    brand: str
    price: float
    size: int
    description: str
    image_url: Optional[str] = None

@dataclass
class ChatMessage:
    id: int
    user_message: str
    bot_response: str
    timestamp: datetime

@dataclass
class ChatContext:
    last_product_viewed: Optional[Product] = None
