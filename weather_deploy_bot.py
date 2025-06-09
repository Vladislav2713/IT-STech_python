import asyncio
import aiohttp
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

async def get_coordinates(city: str) -> tuple:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1") as response:
            data = await response.json()
            if not data.get('results'):
                return None
            return (data['results'][0]['latitude'], data['results'][0]['longitude'])

async def get_weather(lat: float, lon: float) -> dict:
    async with aiohttp.ClientSession() as session:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
        async with session.get(url) as response:
            return await response.json()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Укажи город: /weather <город>")

@dp.message(Command("weather"))
async def get_weather_command(message: Message):
    city = message.get_args().strip()
    if not city:
        return await message.reply("Укажи город!")
    try:
        coords = await get_coordinates(city)
        if not coords:
            return await message.reply("Город не найден!")
        weather_data = await get_weather(*coords)
        current = weather_data['current']
        weather_codes = {
            0: "Ясно", 1: "Преимущественно ясно", 2: "Переменная облачность",
            3: "Пасмурно", 45: "Туман", 48: "Инейный туман"
        }
        desc = weather_codes.get(current['weather_code'], "Неизвестно")
        await message.reply(
            f"Погода в {city}:\n"
            f"Температура: {current['temperature_2m']}°C\n"
            f"Состояние: {desc}"
        )
    except Exception as e:
        await message.reply(f"Ошибка: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())