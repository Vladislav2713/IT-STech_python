import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
API_TOKEN = '8080323721:AAHirhkSn0BEiqkTytuOkIWMFZw_zJBxEyc'  # Замените на ваш токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Отправь текст, и я посчитаю слова!")
@dp.message()
async def count_words(message: Message):
    if message.text:
        words = len(message.text.split())
        await message.answer(f"В сообщении {words} слов(а).")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())