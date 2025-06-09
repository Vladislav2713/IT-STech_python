import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

API_TOKEN = '8080323721:AAHirhkSn0BEiqkTytuOkIWMFZw_zJBxEyc'  # Замените на реальный токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
analyzer = SentimentIntensityAnalyzer()
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Отправь текст, и я определю его настроение!")
@dp.message()
async def analyze_sentiment(message: Message):
    if message.text:
        scores = analyzer.polarity_scores(message.text)
        sentiment = "позитивное" if scores['compound'] >= 0 else "негативное"
        await message.answer(
            f"Настроение: {sentiment}\n"
            f"Детали:\n"
            f"Позитивность: {scores['pos']:.2f}\n"
            f"Негативность: {scores['neg']:.2f}\n"
            f"Нейтральность: {scores['neu']:.2f}"
        )
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())