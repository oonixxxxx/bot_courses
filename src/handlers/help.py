from aiogram.types import CallbackQuery
from keyboards import create_main_keyboard

async def show_help(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "ℹ <b>Помощь</b>\n\n"
        "1. Выберите категорию товаров\n"
        "2. Листайте товары с помощью кнопок\n"
        "3. Возвращайтесь в меню в любой момент\n\n"
        "Для начала работы нажмите /start",
        reply_markup=create_main_keyboard(),
        parse_mode="HTML"
    )
    await callback_query.answer()

def register_help_handlers(dp):
    dp.callback_query.register(show_help, lambda c: c.data == "help")