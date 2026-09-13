import os
import sqlite3
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

def menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎮 Start Game"), KeyboardButton(text="🛒 Shop")],
            [KeyboardButton(text="🎒 My Equipment"), KeyboardButton(text="⚔️ Attack")],
            [KeyboardButton(text="🛡️ Defense"), KeyboardButton(text="🏭 My Economy")],
            [KeyboardButton(text="🗺️ World Map"), KeyboardButton(text="🏆 Leaderboard")],
            [KeyboardButton(text="📜 Game Rules"), KeyboardButton(text="👑 Game Owner")],
            [KeyboardButton(text="⚙️ Settings")]
        ],
        resize_keyboard=True
    )

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🌍⚔️ به World War خوش آمدی!\n\n"
        "💰 پول اولیه: 5M\n"
        "🛢️ نفت: 0\n"
        "🪖 ارتش: 0\n"
        "🗺️ فتح: 0\n\n"
        "برای شروع بازی یکی از گزینه‌ها را انتخاب کن.",
        reply_markup=menu()
    )

@dp.message(F.text == "🎮 Start Game")
async def game(message: Message):
    await message.answer("🎮 شروع بازی\n\nمرحله انتخاب کشور به‌زودی فعال می‌شود.")

@dp.message(F.text == "🛒 Shop")
async def shop(message: Message):
    await message.answer(
        "🛒 فروشگاه\n\n"
        "🏭 تجهیزات درآمدزایی\n"
        "🚜 تانک\n"
        "✈️ جنگنده\n"
        "💣 بمب‌افکن\n"
        "🚢 کشتی جنگی\n"
        "🛳️ ناو هواپیمابر\n"
        "🛡️ پدافند\n"
        "🚀 موشک\n"
        "🔫 سلاح\n"
        "🛢️ نفت"
    )

@dp.message(F.text == "🎒 My Equipment")
async def equipment(message: Message):
    await message.answer("🎒 تجهیزات من\n\nفعلاً تجهیزاتی نداری.")

@dp.message(F.text == "⚔️ Attack")
async def attack(message: Message):
    await message.answer("⚔️ بخش حمله در حال ساخت است.")

@dp.message(F.text == "🛡️ Defense")
async def defense(message: Message):
    await message.answer("🛡️ بخش دفاع در حال ساخت است.")

@dp.message(F.text == "🏭 My Economy")
async def economy(message: Message):
    await message.answer(
        "🏭 اقتصاد من\n\n"
        "💰 پول: 5M\n"
        "🛢️ نفت: 0\n\n"
        "🏪 مغازه کوچک: 100K → 250K/day\n"
        "🏬 مغازه بزرگ: 250K → 550K/day\n"
        "🏭 کارخانه: 1M → 2M/day\n"
        "🏢 شرکت: 3.5M → 5M/day\n"
        "🏦 بانک: 10M → 15M/day\n"
        "🛢️ پالایشگاه: 30M → 50M/day\n"
        "⚡ نیروگاه بزرگ: 270M → 50M/day"
    )

@dp.message(F.text == "🗺️ World Map")
async def world_map(message: Message):
    await message.answer("🗺️ نقشه جهان\n\n۲۰ کشور در بازی وجود دارد.")

@dp.message(F.text == "🏆 Leaderboard")
async def leaderboard(message: Message):
    await message.answer("🏆 لیدربورد\n\nهنوز بازیکنی ثبت نشده است.")

@dp.message(F.text == "📜 Game Rules")
async def rules(message: Message):
    await message.answer(
        "📜 قوانین World War 🌍⚔️\n\n"
        "• حداکثر ۲۰ بازیکن در هر اتاق\n"
        "• هر کشور فقط یک بازیکن\n"
        "• شروع با 5M پول\n"
        "• شروع با 0 نفت\n"
        "• هدف اصلی: فتح کشورها\n"
        "• بازیکن با از دست دادن کشورش OUT می‌شود."
    )

@dp.message(F.text == "👑 Game Owner")
async def owner(message: Message):
    await message.answer("👑 مالک World War\n\nسازنده و مدیر اصلی بازی.")

@dp.message(F.text == "⚙️ Settings")
async def settings(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("❌ این بخش فقط برای مالک بازی است.")
        return

    await message.answer(
        "👑 پنل مدیریت\n\n"
        "تمام قیمت‌ها، قدرت‌ها، قوانین، XP، نفت، زمان‌ها و جوایز "
        "قابل تنظیم توسط مالک خواهند بود."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
