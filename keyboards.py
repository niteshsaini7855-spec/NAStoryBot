from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import INSTAGRAM_LINK, YOUTUBE_LINK

def get_main_keyboard() -> InlineKeyboardMarkup:
    """Returns the main interactive menu for the user using aiogram."""
    keyboard = [
        [InlineKeyboardButton(text="💳 Payment (₹50)", callback_data="payment")],
        [InlineKeyboardButton(text="📤 Send Screenshot", callback_data="screenshot")],
        [InlineKeyboardButton(text="📷 Instagram", url=INSTAGRAM_LINK), 
         InlineKeyboardButton(text="📺 YouTube", url=YOUTUBE_LINK)],
        [InlineKeyboardButton(text="👨‍💻 Contact Admin", callback_data="admin")],
        [InlineKeyboardButton(text="ℹ️ About", callback_data="about")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_back_keyboard() -> InlineKeyboardMarkup:
    """Returns a 'Back to Menu' button for better UX."""
    keyboard = [[InlineKeyboardButton(text="🔙 Back to Main Menu", callback_data="main_menu")]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)