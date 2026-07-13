import logging
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
import keyboards as kb
from config import ADMIN1_ID, ADMIN2_ID

router = Router()
logger = logging.getLogger(__name__)

@router.message(CommandStart())
async def start_command(message: Message):
    """Handles the /start command."""
    welcome_text = (
        "👋 **Welcome To NA Story Hub**\n\n"
        "🔒 **Premium Private Channel Access**\n\n"
        "💰 ₹50 Payment करें और Screenshot भेजें।\n"
        "Admin Verify करने के बाद आपको Private Channel का Link milega."
    )
    await message.answer(text=welcome_text, reply_markup=kb.get_main_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "main_menu")
async def handle_main_menu(query: CallbackQuery):
    await query.answer()
    welcome_text = (
        "👋 **Welcome To NA Story Hub**\n\n"
        "🔒 **Premium Private Channel Access**\n\n"
        "💰 ₹50 Payment करें और Screenshot भेजें।"
    )
    await query.message.edit_text(text=welcome_text, reply_markup=kb.get_main_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "payment")
async def handle_payment(query: CallbackQuery):
    await query.answer()
    try:
        # aiogram handle images safely using FSInputFile without keeping locks
        photo = FSInputFile("images/qr.jpg")
        await query.message.answer_photo(
            photo=photo,
            caption="✨ **NA Story Hub - Premium Access**\n\n👉 upper diye gaye QR Code ko scan karke **₹50** pay karein aur uska clear screenshot le lein.",
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"QR Image error: {e}")
        await query.message.answer("⚠️ Payment QR currently unavailable. Contact Admin.")

@router.callback_query(F.data == "screenshot")
async def handle_screenshot(query: CallbackQuery):
    await query.answer()
    instruction = (
        "📤 **Screenshot Kaise Bhejein?**\n\n"
        "1. Payment successful hone ke baad admin ko direct DM karein.\n"
        f"2. Aap in Admins ko contact kar sakte hain:\n"
        f"   • Admin 1: {ADMIN1_ID}\n"
        f"   • Admin 2: {ADMIN2_ID}\n\n"
        "Verification ke baad 5-10 mins me link mil jayega."
    )
    await query.message.edit_text(text=instruction, reply_markup=kb.get_back_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "admin")
async def handle_admin(query: CallbackQuery):
    await query.answer()
    admin_text = (
        "👨‍💻 **Need Help? Contact Admins Directly:**\n\n"
        f"🚀 Admin 1: {ADMIN1_ID}\n"
        f"⚡ Admin 2: {ADMIN2_ID}\n\n"
        "Kisi bhi issues ya queries ke liye direct message karein."
    )
    await query.message.edit_text(text=admin_text, reply_markup=kb.get_back_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "about")
async def handle_about(query: CallbackQuery):
    await query.answer()
    about_text = (
        "ℹ️ **About NA Story Hub**\n\n"
        "Hum provide karte hain premium content aur exclusive private stories.\n"
        "Join karke aap unique, high-quality material access kar sakte hain."
    )
    await query.message.edit_text(text=about_text, reply_markup=kb.get_back_keyboard(), parse_mode="Markdown")