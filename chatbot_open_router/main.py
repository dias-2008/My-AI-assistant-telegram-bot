import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler as TelegramMessageHandler, filters
from config import TELEGRAM_TOKEN
from handlers.command_handler import CommandHandler
from handlers.message_handler import MessageHandler
from telegram.error import NetworkError, TimedOut
import asyncio

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def run_bot():
    # Initialize bot application
    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .build()
    )
    
    # Initialize handlers
    command_handler = CommandHandler()
    message_handler = MessageHandler()
    
    # Add command handlers
    application.add_handler(TelegramMessageHandler(filters.COMMAND & filters.Regex('^/start'), command_handler.start))
    application.add_handler(TelegramMessageHandler(filters.COMMAND & filters.Regex('^/help'), command_handler.help))
    
    # Add message handler for all other messages
    application.add_handler(TelegramMessageHandler(filters.TEXT & ~filters.COMMAND, message_handler.handle_message))
    
    # Error handler
    async def error_handler(update, context):
        logger.error(f"Error occurred: {context.error}")
        if isinstance(context.error, (NetworkError, TimedOut)):
            logger.info("Network error occurred. Retrying...")
            await asyncio.sleep(1)
            return
        
    application.add_error_handler(error_handler)
    
    logger.info("Starting bot...")
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    try:
        run_bot()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")