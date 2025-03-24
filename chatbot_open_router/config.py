import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# OpenRouter API endpoints
OPENROUTER_API_URL = "https://openrouter.ai/api/v1"
CHAT_ENDPOINT = f"{OPENROUTER_API_URL}/chat/completions"
IMAGE_ENDPOINT = f"{OPENROUTER_API_URL}/images/generations"