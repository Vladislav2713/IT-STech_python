import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
API_TOKEN = '8080323721:AAHirhkSn0BEiqkTytuOkIWMFZw_zJBxEyc'  # Замените на ваш токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создание inline-клавиатуры
kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Позитивное", callback_data='positive'),
        InlineKeyboardButton(text="Негативное", callback_data='negative')
    ]
])
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Какое у тебя настроение?", reply_markup=kb)
@dp.callback_query()
async def process_callback(callback_query: CallbackQuery):
    mood = callback_query.data
    await callback_query.message.answer(f"Твоё настроение: {mood}!")
    await callback_query.answer()  # Закрыть callback

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())