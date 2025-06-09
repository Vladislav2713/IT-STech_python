import asyncio
import os
import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
# Инициализация бота
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("📰 Получить новости: /news <тема>")
@dp.message(Command("news"))
async def get_news(message: Message):
    # Получаем аргументы команды
    args = message.text.split(maxsplit=1)
    topic = args[1] if len(args) > 1 else 'technology'
    # Проверяем API ключ
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        await message.answer("❌ API ключ не найден в .env файле!")
        return
    # Формируем URL запроса
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&pageSize=3&language=ru"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # Обрабатываем статус ответа
                if response.status != 200:
                    return await message.answer(f"⚠️ Ошибка API: {response.status}")
                # Парсим JSON
                data = await response.json()
                articles = data.get('articles', [])
                # Формируем ответ
                if not articles:
                    return await message.answer("🔍 Новостей по этой теме не найдено")
                response_text = "📌 Последние новости:\n\n"
                for i, article in enumerate(articles[:3], 1):
                    title = article['title'][:150] + '...' if len(article['title']) > 150 else article['title']
                    response_text += f"{i}. {title}\n{article['url']}\n\n"
                await message.answer(response_text)
                
    except Exception as e:
        await message.answer(f"🚨 Произошла ошибка: {str(e)}")

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())