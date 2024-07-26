import asyncio
from mailbox import Message
from aiogram import Bot, Dispatcher, F
from aiogram.client import bot
from aiogram.types import FSInputFile

async def send_images(bot: Bot, message: Message, photo_paths):
    for photo_path in photo_paths:
        await message.answer_photo(FSInputFile(photo_path))
        await asyncio.sleep(20)

async def send_images_periodically(bot: Bot, message: Message, photo_paths, interval=20):

    while True:
        await send_images(bot, message, photo_paths)
        await asyncio.sleep(interval)

async def send_welcome(message: Message):
    photo_paths = [
        f"img/1.jpg",
        f"img/2.jpg",
        f"img/3.jpg",
        f"img/4.jpg",
        f"img/5.jpg",
        f"img/6.jpg",
        f"img/7.jpg"
    ]

    await asyncio.create_task(send_images_periodically(bot, message, photo_paths))

def register_image(dp: Dispatcher):
    dp.message.register(send_welcome, F.text=="/image")


