from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from catalog import catalog

def create_categories_keyboard():
    buttons = []
    for category in catalog.keys():
        buttons.append([InlineKeyboardButton(text=category, callback_data=f"category_{category}")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)