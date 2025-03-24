class IntentDetector:
    def detect_intent(self, message: str) -> str:
        message = message.lower()
        
        # Check for image generation intent
        if any(keyword in message for keyword in ["create image", "generate image", "draw", "create a picture"]):
            return "image"
            
        # Check for code-related intent
        if any(keyword in message for keyword in ["code", "function", "program", "debug", "write a"]):
            return "code"
            
        # Check for translation intent
        if any(keyword in message for keyword in ["translate", "translation"]):
            return "translation"
            
        # Default to general chat
        return "chat"