from src.infrastructure.db.database import SessionLocal, Base, engine
from src.infrastructure.db.models import ProductORM

Base.metadata.create_all(bind=engine)

db = SessionLocal()

shoes = [
    ProductORM(name="Air Max 90", brand="Nike", price=120.0, size=42,
               description="Zapatillas deportivas clásicas con amortiguación Air.", image_url="https://example.com/airmax90.jpg"),
    ProductORM(name="Ultraboost", brand="Adidas", price=180.0, size=43,
               description="Zapatillas para correr con gran comodidad.", image_url="https://example.com/ultraboost.jpg"),
    ProductORM(name="Classic Leather", brand="Reebok", price=90.0, size=41,
               description="Estilo retro con confort moderno.", image_url="https://example.com/reebok.jpg")
]

db.add_all(shoes)
db.commit()
db.close()
print("✅ Datos iniciales cargados")
