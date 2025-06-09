import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
API_TOKEN = '8080323721:AAHirhkSn0BEiqkTytuOkIWMFZw_zJBxEyc'  # Замените на токен от BotFather
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот на aiogram.")
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Команды:\n/start - Приветствие\n/help - Справка")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())