import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties
from config import API_TOKEN
from handlers.finish_handler import register_finish_handlers, finish_command
from handlers.images import register_image
from handlers.start_handler import register_start_handlers, start_command
from handlers.callback_handler import register_callback_handlers
from handlers.hint_handler import register_hint_handlers

# Инициализация бота с параметрами по умолчанию
session = AiohttpSession()
bot = Bot(token=API_TOKEN, session=session,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация хендлеров
register_start_handlers(dp)
register_callback_handlers(dp)
register_hint_handlers(dp)
register_finish_handlers(dp)  # Здесь регистрируем hint_handlers
register_image(dp)


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))  # Use asyncio.run for better practice

