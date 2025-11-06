from fastapi import FastAPI, Depends
from src.infrastructure.db.database import get_db
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.llm_providers.gemini_service import GeminiService
from src.application.product_service import ProductService
from src.application.chat_service import ChatService

app = FastAPI(title="E-commerce Chat AI")

@app.get("/products")
def list_products(db=Depends(get_db)):
    repo = ProductRepository(db)
    service = ProductService(repo)
    return service.list_products()

@app.post("/chat")
def chat(user_message: str):
    chat_service = ChatService(chat_repo=None, llm=GeminiService())  # puedes conectar un repo real después
    return {"response": chat_service.chat(user_message)}
