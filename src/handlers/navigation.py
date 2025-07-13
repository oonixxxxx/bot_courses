from aiogram.types import CallbackQuery
from catalog import catalog
from .items import show_item

async def navigate_items(callback_query: CallbackQuery):
    action, category = callback_query.data.split("_")
    items = catalog[category]
    
    if action == "next":
        items['current_index'] = (items['current_index'] + 1) % len(items['items'])
    else:
        items['current_index'] = (items['current_index'] - 1) % len(items['items'])
    
    await show_item(callback_query.message, category, items['current_index'])
    await callback_query.answer()

def register_navigation_handlers(dp):
    dp.callback_query.register(navigate_items, lambda c: c.data.startswith(("next_", "prev_")))