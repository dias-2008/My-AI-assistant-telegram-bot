from telegram import Update
from telegram.ext import ContextTypes
from services.intent_detector import IntentDetector
from services.openrouter_service import OpenRouterService

class MessageHandler:
    def __init__(self):
        self.intent_detector = IntentDetector()
        self.openrouter_service = OpenRouterService()

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.message.text
        intent = self.intent_detector.detect_intent(message)
        
        await update.message.chat.send_action('typing')
        
        try:
            if "code" in message.lower() or "function" in message.lower():
                # First send the explanation
                prompt_explanation = f"Give a brief explanation for: {message}"
                explanation = await self.openrouter_service.chat_completion(prompt_explanation)
                await update.message.reply_text(explanation)
                
                # Then send the code in a separate message
                prompt_code = f"Provide only the code implementation for: {message}. No explanations, just the code."
                code = await self.openrouter_service.chat_completion(prompt_code)
                
                # Clean and format the code
                code = code.replace('```python', '').replace('```', '').strip()
                formatted_code = f"```python\n{code}\n```"
                
                # Send code as a separate message
                await update.message.reply_text(formatted_code, parse_mode='Markdown')
            else:
                response = await self.openrouter_service.chat_completion(message)
                await update.message.reply_text(response)
                
        except Exception as e:
            await update.message.reply_text(f"Sorry, an error occurred: {str(e)}")