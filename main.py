import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start

async def main() -> None:
    print("Бот начал работу")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())