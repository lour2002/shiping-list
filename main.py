import gkeepapi
import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot
from telegram.constants import ParseMode

# Load .env file only if it exists (for local development)
load_dotenv()

master_token = os.getenv('MASTER_TOKEN')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
telegram_chat_thread_id = 2

# Debug: Check if environment variables are loaded
print("MASTER_TOKEN:", "✓ Loaded" if master_token else "✗ Missing")
print("TELEGRAM_BOT_TOKEN:", "✓ Loaded" if telegram_bot_token else "✗ Missing")
print("TELEGRAM_CHAT_ID:", "✓ Loaded" if telegram_chat_id else "✗ Missing")

keep = gkeepapi.Keep()
device_id = "2811a82c0609"

print(f"Using device_id: {device_id}")
print("Authenticating with Google Keep...")

keep.authenticate('borisdiaw12@gmail.com', master_token, None, None, device_id)

keep.sync()
shoppinglist = keep.get('1NopFGnUhEvmKthvjAlqejRUL_xQXHEsNU0mSQEaLn5ijfukEQowKdzQ1wjTZ1Q')

list_items = []
for item in shoppinglist.unchecked:
    list_items.append(f"☐ {item.text}")

if not list_items:
    message = "📝 Список покупок пуст"
else:
    message = "🛒 *Список покупок:*\n\n" + "\n".join(list_items)

print(f"\nПодготовлено сообщение:\n{message}\n")


async def send_telegram_message():
    """Отправка сообщения в Telegram"""
    bot = Bot(token=telegram_bot_token)
    try:
        await bot.send_message(
            chat_id=telegram_chat_id,
            text=message,
            parse_mode=ParseMode.MARKDOWN,
            message_thread_id=telegram_chat_thread_id
        )
        print("✓ Сообщение успешно отправлено в Telegram")
        return True
    except Exception as e:
        print(f"✗ Ошибка отправки в Telegram: {e}")
        return False


# Отправка сообщения
success = asyncio.run(send_telegram_message())

if success:
    # Очищаем список покупок только если сообщение успешно отправлено
    for item in shoppinglist.unchecked:
        item.delete()
    keep.sync()
    print("✓ Список покупок очищен")
else:
    print("✗ Список не был очищен из-за ошибки отправки")
