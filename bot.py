import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
text = "👋 Вітаю! Це 'Гра від колоди🎮'!"


"
    text += "📜 Доступні команди:
"
    text += "/join - приєднатися до гри
"
    text += "/leave - вийти з гри
"
    text += "/play - почати гру
"
    text += "/players - список гравців
"
    await message.answer(text)

@dp.message_handler(commands=['join'])
async def join_game(message: types.Message):
    await message.answer(f"{message.from_user.first_name} приєднався(-лась) до гри!")

@dp.message_handler(commands=['leave'])
async def leave_game(message: types.Message):
    await message.answer(f"{message.from_user.first_name} вийшов(-ла) з гри!")

@dp.message_handler(commands=['play'])
async def play_game(message: types.Message):
    await message.answer("🎮 Починаємо гру...")

@dp.message_handler(commands=['players'])
async def show_players(message: types.Message):
    await message.answer("📋 Гравці: (тимчасово тестовий список)
- Player1
- Player2")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
