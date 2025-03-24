import requests
import json
from config import OPENROUTER_API_KEY

class OpenRouterService:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/",
        }
        self.base_url = "https://openrouter.ai/api/v1"

    async def chat_completion(self, prompt, model="openai/gpt-3.5-turbo"):
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error in chat completion: {str(e)}"

    async def advanced_completion(self, prompt, model="anthropic/claude-3-opus"):
        """For more complex tasks using a more capable model"""
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2000,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error in advanced completion: {str(e)}"

    async def generate_image(self, prompt):
        payload = {
            "model": "anthropic/claude-3-opus",  # Using Claude 3 which has better multimodal capabilities
            "messages": [{
                "role": "user",
                "content": f"Please generate an image based on this description: {prompt}. Respond only with the image, no text."
            }],
            "max_tokens": 1000
        }
        
        try:
            session = requests.Session()
            session.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))
            
            response = session.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            print("Debug - API Response:", result)  # For debugging
            
            # Look for image URL in the response
            if 'choices' in result and result['choices']:
                content = result['choices'][0]['message']['content']
                # Try to find any URLs in the response
                import re
                urls = re.findall('https?://[^\s<>"]+|www\.[^\s<>"]+', content)
                if urls:
                    return urls[0]
            
            raise Exception("No image URL found in response")
        except Exception as e:
            print(f"Debug - Full error: {str(e)}")  # Debug line
            return f"Error: {str(e)}"