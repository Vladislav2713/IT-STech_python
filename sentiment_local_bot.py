import asyncio
import os
from textblob import TextBlob
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("📝 Отправь текст на английском для анализа настроения!")
@dp.message()
async def analyze_sentiment(message: Message):
    text = message.text.strip()
    if not text:
        return await message.answer("❌ Текст не может быть пустым!")
    
    try:
        # Анализ тональности через TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        # Определение метки
        if polarity > 0.2:
            label = "😃 Позитивное"
        elif polarity < -0.2:
            label = "😠 Негативное"
        else:
            label = "😐 Нейтральное"
        await message.answer(
            f"{label}\n"
            f"Уверенность: {abs(polarity):.2f}"
        )
    except Exception as e:
        await message.answer(f"🚨 Ошибка анализа: {str(e)}")

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())