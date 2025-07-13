from aiogram.types import CallbackQuery
from catalog import catalog, current_category
from keyboards import create_items_keyboard

async def show_item(message, category, item_index):
    items = catalog[category]
    item = items['items'][item_index]
    price = items['prices'][item_index]
    description = items['descriptions'][item_index]
    
    text = (f"<b>{category}: {item}</b>\n\n"
            f"<i>{description}</i>\n\n"
            f"Год: <b>{price}$</b>\n\n"
            f"Курс {item_index + 1} из {len(items['items'])}")
    
    await message.edit_text(
        text,
        reply_markup=create_items_keyboard(category),
        parse_mode="HTML"
    )

async def show_category_items(callback_query: CallbackQuery):
    category = callback_query.data.split("_")[1]
    current_category = category
    items = catalog[category]
    
    await show_item(callback_query.message, category, items['current_index'])
    await callback_query.answer()

def register_items_handlers(dp):
    dp.callback_query.register(show_category_items, lambda c: c.data.startswith("category_"))