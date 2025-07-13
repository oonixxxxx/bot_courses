from .start import register_start_handlers
from .categories import register_categories_handlers
from .items import register_items_handlers
from .navigation import register_navigation_handlers
from .help import register_help_handlers

def register_handlers(dp):
    register_start_handlers(dp)
    register_categories_handlers(dp)
    register_items_handlers(dp)
    register_navigation_handlers(dp)
    register_help_handlers(dp)