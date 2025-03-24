from telegram import Update
from telegram.ext import ContextTypes

class CommandHandler:
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_message = (
            "👋 Hello! I'm your AI assistant powered by OpenRouter.\n\n"
            "I can help you with:\n"
            "✏️ Writing and debugging code\n"
            "🎨 Generating images\n"
            "💬 Answering questions\n"
            "📝 Writing and analysis\n"
            "🔧 Technical support\n"
            "🌐 Language translation\n\n"
            "Just send me your request, and I'll do my best to help!"
        )
        await update.message.reply_text(welcome_message)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_message = (
            "🔹 Example commands:\n\n"
            "- 'Write a Python function to sort a list'\n"
            "- 'Generate an image of a sunset'\n"
            "- 'Translate Hello to Spanish'\n"
            "- 'Help me debug this code...'\n"
            "- 'Explain how databases work'\n\n"
            "Just type your question or request naturally!"
        )
        await update.message.reply_text(help_message)