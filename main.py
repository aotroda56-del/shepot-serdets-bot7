from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import asyncio

TOKEN = "8445444619:AAFdR4jF1IQJzEFlL_DsJ-JTxT9nwkwwC58"  # твій токен
ADMIN_CHAT_ID = -1003120877184  # ID адміна або групи

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Старт
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет!\n"
        "Рад тебя видеть! 💫\n"
        "Я — бот *Шепот сердец 💌*\n\n"
        "Можешь написать своё сообщение — администратор скоро тебе ответит.",
        parse_mode="Markdown"
    )

# Пересилання від користувачів адміну
@dp.message(lambda m: m.chat.id != ADMIN_CHAT_ID)
async def forward_to_admin(message: Message):
    user_id = message.from_user.id
    username = f"@{message.from_user.username}" if message.from_user.username else "без_юзернейма"
    text = f"📩 Сообщение от {username} (ID: {user_id}):\n\n{message.text or '[не текстовое сообщение]'}"
    await bot.send_message(ADMIN_CHAT_ID, text)

# Відповідь від адміна
@dp.message(lambda m: m.chat.id == ADMIN_CHAT_ID and m.reply_to_message)
async def reply_to_user(message: Message):
    try:
        original_text = message.reply_to_message.text
        user_id = int(original_text.split('ID:')[1].split(')')[0])
        await bot.send_message(user_id, message.text)
    except Exception as e:
        await message.reply(f"⚠️ Ошибка: {e}")

# Запуск бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if name == "main":
    asyncio.run(main())
