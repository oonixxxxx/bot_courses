from aiogram.types import CallbackQuery
from keyboard import create_categories_keyboard

async def show_categories(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Выберите категорию товаров:",
        reply_markup=create_categories_keyboard()
    )
    await callback_query.answer()

async def back_to_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Главное меню:",
        reply_markup=create_main_keyboard()
    )
    await callback_query.answer()

def register_categories_handlers(dp):
    dp.callback_query.register(show_categories, lambda c: c.data == "categories")
    dp.callback_query.register(back_to_menu, lambda c: c.data == "back_to_menu")