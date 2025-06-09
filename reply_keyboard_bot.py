import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
API_TOKEN = '8080323721:AAHirhkSn0BEiqkTytuOkIWMFZw_zJBxEyc'  # Замените на токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создание клавиатуры (
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Выбери действие:", reply_markup=kb)
@dp.message(lambda message: message.text == "Привет")
async def greet(message: Message):
    await message.answer("Привет, пользователь!")
@dp.message(lambda message: message.text == "Помощь")
async def help_message(message: Message):
    await message.answer("Я бот с клавиатурой!")

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())