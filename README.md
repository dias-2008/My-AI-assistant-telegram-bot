# My AI Assistant Telegram Bot

A powerful Telegram bot powered by OpenRouter API that provides intelligent conversations, code generation, and more.

## Features
- 💬 Smart AI conversations using GPT models
- 💻 Code generation with explanations
- 📝 Clean, copy-pasteable code blocks
- ⚡ Fast response times
- 🔒 Secure token handling

## Prerequisites
- Python 3.8 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- OpenRouter API Key (from [OpenRouter](https://openrouter.ai/))

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dias-2008/My-AI-assistant-telegram-bot.git
   cd My-AI-assistant-telegram-bot
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your tokens:
   ```plaintext
   TELEGRAM_TOKEN=your_telegram_token_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

## Usage
1. Start the bot:
   ```bash
   python main.py
   ```
2. Open Telegram and search for your bot using its username.
3. Start a conversation with `/start`.
4. Try these commands:
   - `/help` - Show available commands
   - Ask any question
   - Request code examples by including "code" or "function" in your message

## Code Generation Examples
Request a simple function:
```plaintext
write a function to calculate factorial
```
Request specific code:
```plaintext
code for bubble sort in python
```
The bot will provide:
- A brief explanation of the code
- Clean, formatted, copy-pasteable code block

## Project Structure
```plaintext
chatbot_open_router/
├── main.py                 # Main bot application
├── config.py              # Configuration handling
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (create this)
├── .gitignore             # Git ignore rules
├── handlers/              # Message and command handlers
│   ├── __init__.py
│   ├── command_handler.py
│   └── message_handler.py
└── services/              # Core services
    ├── __init__.py
    ├── intent_detector.py
    └── openrouter_service.py
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- OpenRouter for providing the AI API
- `python-telegram-bot` for the Telegram bot framework

## Contact
- **Dias** - @GitHub
- **Project Link**: [My AI Assistant Telegram Bot](https://github.com/dias-2008/My-AI-assistant-telegram-bot)
