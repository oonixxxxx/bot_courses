from aiogram.filters import Command
from aiogram.types import Message
from keyboard import create_main_keyboard

async def send_welcome(message: Message):
    await message.answer(
        "Добро пожаловать в наш магазин! Выберите действие:",
        reply_markup=create_main_keyboard()
    )

def register_start_handlers(dp):
    dp.message.register(send_welcome, Command('start'))