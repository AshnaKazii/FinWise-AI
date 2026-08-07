import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL_NAME", "openai/gpt-oss-20b")


def ask_ai(question):

    if not API_KEY:
        return "❌ OpenRouter API key not found. Add it to your .env file."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "FinWise AI"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are FinWise AI, a professional personal finance assistant. "
                    "Provide clear, practical, beginner-friendly financial guidance. "
                    "Use the user's financial data whenever available. "
                    "Avoid legal or tax advice."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ API Error: {str(e)}"