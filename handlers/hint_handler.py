from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import show_hint_by_id


async def send_hint(message: types.Message):
    hint_id = 1
    hints = show_hint_by_id(hint_id)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=hint_text, callback_data=f"hint_{hint_id}")]
            for hint_id, hint_text in hints
        ]
    )

    await message.reply("Выберите подсказку:", reply_markup=keyboard)


def register_hint_handlers(dp: Dispatcher):
    dp.message.register(send_hint, Command(commands=["hint"]))
