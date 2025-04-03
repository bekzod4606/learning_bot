import asyncio

from aiogram import Bot, Dispatcher
from functions import get_user_info


TOKEN = "7833868916:AAF8BoJ2IcTkHDXPugGWGxWOMcFSx5L2uQM"

if not TOKEN:
    raise ValueError("Bot token is not set! Please set the BOT_TOKEN environment variable or hardcode it.")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

async def on_startup(bot: Bot):
    await bot.send_message(1064272609, "Bot started! ")

async def main():
    dp.startup.register(on_startup)
    dp.message.register(get_user_info)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
