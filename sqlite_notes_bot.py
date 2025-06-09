import asyncio
import sqlite3
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
API_TOKEN = '8080323721:AAHirhkSn0BEiqkTytuOkIWMFZw_zJBxEyc'  # Замените на ваш токен

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (user_id INTEGER, note TEXT, date TEXT)''')
    conn.commit()
    return conn
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
conn = init_db()
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Добавь заметку: /addnote <текст>")
@dp.message(Command("addnote"))
async def add_note(message: Message):
    user_id = message.from_user.id
    note = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not note:
        return await message.answer("Укажи текст заметки!")
    date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        with conn:
            conn.execute("INSERT INTO notes VALUES (?, ?, ?)", 
                        (user_id, note, date))
        await message.answer("Заметка добавлена!")
    except sqlite3.Error as e:
        await message.answer(f"Ошибка: {str(e)}")
@dp.message(Command("listnotes"))
async def list_notes(message: Message):
    user_id = message.from_user.id

    try:
        with conn:
            cursor = conn.execute("SELECT note, date FROM notes WHERE user_id = ?", 
                                 (user_id,))
            notes = cursor.fetchall()
        if notes:
            response = "\n".join([f"• {note} ({date})" for note, date in notes])
            await message.answer(response)
        else:
            await message.answer("Заметок нет!")
    except sqlite3.Error as e:
        await message.answer(f"Ошибка: {str(e)}")

async def on_shutdown():
    conn.close()
    await bot.close()

async def main():
    await dp.start_polling(bot, on_shutdown=on_shutdown)
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass