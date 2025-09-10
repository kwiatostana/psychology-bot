from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

from handlers.users import users_router

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN', ''))
    dp = Dispatcher()
    dp.include_routers(users_router)
    print('бот запущен')
    await bot.delete_webhook(True)
    await dp.start_polling(bot)

asyncio.run(main())
 