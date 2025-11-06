import os
import google.generativeai as genai

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-pro")

    def generate_response(self, user_message: str) -> str:
        prompt = f"El usuario pregunta: {user_message}\nSugiere zapatos adecuados según su necesidad."
        response = self.model.generate_content(prompt)
        return response.text.strip()
