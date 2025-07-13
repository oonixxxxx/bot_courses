from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_main_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Категории товаров", callback_data="categories")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)