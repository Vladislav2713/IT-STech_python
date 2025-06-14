import os
import sqlite3
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

def init_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (user_id INTEGER, note TEXT, date TEXT)")
    conn.commit()
    return conn

conn = init_db()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Команды: /addnote <текст>, /listnotes, /deletenote <номер>")

@dp.message(Command("addnote"))
async def add_note(message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    note = args[1].strip() if len(args) > 1 else ""
    
    if not note:
        return await message.answer("❌ Укажи текст заметки!")
    
    date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO notes VALUES (?, ?, ?)", (user_id, note, date))
        await message.answer("✅ Заметка добавлена!")
    except Exception as e:
        await message.answer(f"⚠️ Ошибка: {str(e)}")

@dp.message(Command("listnotes"))
async def list_notes(message: Message):
    user_id = message.from_user.id
    c = conn.cursor()
    c.execute("SELECT rowid, note, date FROM notes WHERE user_id = ?", (user_id,))
    notes = c.fetchall()
    if notes:
        response = "\n".join(f"{rowid}. {note} ({date})" for rowid, note, date in notes)
        await message.reply(response)
    else:
        await message.reply("Заметок нет!")

@dp.message(Command("deletenote"))
async def delete_note(message: Message):
    user_id = message.from_user.id
    try:
        note_id = int(message.get_args().strip())
        c = conn.cursor()
        c.execute("DELETE FROM notes WHERE rowid = ? AND user_id = ?", (note_id, user_id))
        if c.rowcount:
            conn.commit()
            await message.reply("Заметка удалена!")
        else:
            await message.reply("Заметка не найдена!")
    except ValueError:
        await message.reply("Укажи номер заметки!")

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        conn.close()

if __name__ == "__main__":
    asyncio.run(main())