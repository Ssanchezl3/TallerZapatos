from src.domain.entities import ChatMessage
from src.domain.repositories import IChatRepository
from src.infrastructure.llm_providers.gemini_service import GeminiService

class ChatService:
    def __init__(self, chat_repo: IChatRepository, llm: GeminiService):
        self.chat_repo = chat_repo
        self.llm = llm

    def chat(self, user_message: str) -> str:
        bot_response = self.llm.generate_response(user_message)
        chat_message = ChatMessage(id=0, user_message=user_message, bot_response=bot_response)
        self.chat_repo.save_message(chat_message)
        return bot_response
