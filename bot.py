import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = "8589710012:AAG39AwCJDMYap31QZBbVzdv_ZcIXYNyRig"
JAP_API_KEY = "dc5610ff7052537d86131877140b9c58"
JAP_API_URL = "https://justanotherpanel.com/api/v2"
ADMIN_ID = 123456789

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

class OrderState(StatesGroup):
    waiting_link = State()
    waiting_quantity = State()

user_service = {}

def main_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 Telegram Premium", callback_data="cat_tg_premium")],
        [InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="cat_tg_stars")],
        [InlineKeyboardButton(text="📱 Telegram Nomer", callback_data="cat_tg_nomer")],
        [InlineKeyboardButton(text="📈 Telegram Nakrutka", callback_data="cat_tg_nakrutka")],
        [InlineKeyboardButton(text="📸 Instagram Nakrutka", callback_data="cat_ig_nakrutka")],
        [InlineKeyboardButton(text="▶️ YouTube Nakrutka", callback_data="cat_yt_nakrutka")],
        [InlineKeyboardButton(text="💰 Balans", callback_data="balance")],
    ])
    return kb

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 <b>Fetty SMM Bot</b>ga xush kelibsiz!\n\n"
        "Quyidagi xizmatlardan birini tanlang:",
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "balance")
async def balance(call: types.CallbackQuery):
    await call.message.answer("💰 Sizning balansingiz: <b>0 so'm</b>\n\nTez orada to'lov tizimi qo'shiladi!", parse_mode="HTML")

@dp.callback_query(F.data.startswith("cat_"))
async def category(call: types.CallbackQuery):
    cats = {
        "cat_tg_premium": "💎 Telegram Premium xizmatlari tez orada!",
        "cat_tg_stars": "⭐ Telegram Stars xizmatlari tez orada!",
        "cat_tg_nomer": "📱 Telegram Nomer xizmatlari tez orada!",
        "cat_tg_nakrutka": "📈 Telegram Nakrutka - tez orada!",
        "cat_ig_nakrutka": "📸 Instagram Nakrutka - tez orada!",
        "cat_yt_nakrutka": "▶️ YouTube Nakrutka - tez orada!",
    }
    await call.message.answer(cats.get(call.data, "Tez orada!"))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
