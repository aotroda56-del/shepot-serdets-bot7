from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

TOKEN = "8445444619:AAFdR4jF1IQJzEFIL_DsJ-JTxT9nwkwwC58"
ADMIN_CHAT_ID = -1003120877184  # заміни на свій чат адміністраторів

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "👋 Привет!\n"
        "Рад тебя видеть! 💫\n"
        "Я — бот *Шепот сердец 💌*\n\n"
        "Можешь написать своё сообщение — администратор скоро тебе ответит.",
        parse_mode="Markdown"
    )

@dp.message()
async def forward_to_admins(message: Message):
    user_id = message.from_user.id
    username = f"@{message.from_user.username}" if message.from_user.username else "без_юзернейма"
    text = f"📩 Сообщение от {username} (ID: {user_id}):\n\n{message.text or '[не текстовое сообщение]'}"
    await bot.send_message(ADMIN_CHAT_ID, text)

@dp.message()
async def reply_to_user(message: Message):
    # Відповідь користувачу можна реалізувати через окрему логіку в адмін-чаті
    pass

if __name__ == "__main__":
    import asyncio
    from aiogram import F
    from aiogram import Router

    router = Router()
    router.message.register(start_command, F.text.startswith("/start"))
    router.message.register(forward_to_admins)
    dp.include_router(router)

    asyncio.run(dp.start_polling(bot))
