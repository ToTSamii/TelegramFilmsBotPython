import asyncio
from aiogram import Bot, Dispatcher


dp = Dispatcher()


def Tg_Bot(token) -> None:

    bot = Bot(token)
    print("Bot started!")

    async def start_bot() -> None:
        await dp.start_polling(bot)


    asyncio.run(start_bot())