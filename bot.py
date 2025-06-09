import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('7824081044:AAEFACJWhCVPjIFYwNG_-llm953o_EX5eU4'))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Привет! Я развёрнут на Render!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())