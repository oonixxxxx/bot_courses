from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_items_keyboard(category):
    buttons = [
        [
            InlineKeyboardButton(text="⬅️", callback_data=f"prev_{category}"),
            InlineKeyboardButton(text="➡️", callback_data=f"next_{category}")
        ],
        [InlineKeyboardButton(text="Назад к категориям", callback_data="categories")],
        [InlineKeyboardButton(text="Главное меню", callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)