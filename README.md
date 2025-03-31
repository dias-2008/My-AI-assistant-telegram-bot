Let's update the README to include both PC and mobile (Termux) setup instructions:

```markdown:c:\Users\admin\Desktop\Trae_projects\chatbot_open_router\README.md
# My AI Assistant Telegram Bot

A Telegram bot powered by OpenRouter API for smart conversations and code generation.

## Get Your Tokens First
1. Get Telegram Bot Token: Message [@BotFather](https://t.me/BotFather) on Telegram
2. Get OpenRouter API Key: Visit [OpenRouter](https://openrouter.ai/keys)

## PC Setup

### Windows
```bash
git clone https://github.com/dias-2008/My-AI-assistant-telegram-bot.git
cd My-AI-assistant-telegram-bot
pip install -r requirements.txt
```

### Create Config (PC)
Create `config.py` in the project folder:
```python
TELEGRAM_TOKEN = "your_telegram_token"
OPENROUTER_API_KEY = "your_openrouter_key"
```

## Mobile Setup (Android)

### Using Termux
1. Install Termux from F-Droid
2. In Termux, run:
```bash
pkg install python git
git clone https://github.com/dias-2008/My-AI-assistant-telegram-bot.git
cd My-AI-assistant-telegram-bot
pip install -r requirements.txt
```

### Create Config (Mobile)
Use any text editor (like QuickEdit) to create `config.py`:
```python
TELEGRAM_TOKEN = "your_telegram_token"
OPENROUTER_API_KEY = "your_openrouter_key"
```

## Run Bot (Both PC & Mobile)
```bash
python main.py
```

## Features
- 💬 Smart AI chat
- 💻 Code generation
- 🌍 English & Russian support
- ⚡ Fast responses

## Commands
- `/start` - Begin chat
- `/help` - Show features

## Examples
- Ask questions about anything
- Request code: "write a function for..."
- Get explanations in English or Russian

## Need Help?
Contact: [@dias-2008](https://github.com/dias-2008)
```

