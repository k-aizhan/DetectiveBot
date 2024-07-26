from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import show_suspected_by_id


async def finish_command(message: types.Message):
    suspected_buttons = [
        [InlineKeyboardButton(
            text="Леди Сотби",
            callback_data="suspected_1",
        )],
        [InlineKeyboardButton(
            text="Джеймс Реддингтон",
            callback_data="suspected_2",
        )],
        [InlineKeyboardButton(
            text="Роуз Реддингтон",
            callback_data="suspected_3",
        )],
        [InlineKeyboardButton(
            text="Реджинальда Вебстер",
            callback_data="suspected_4",
        )],
        [InlineKeyboardButton(
            text="Владелец",
            callback_data="suspected_5",
        )],
        [InlineKeyboardButton(
            text="Теодор Рив",
            callback_data="suspected_6",
        )]
    ]

    keyboard = InlineKeyboardMarkup(
        type="inline", inline_keyboard=[*suspected_buttons]
    )

    await message.reply("Выберите подозреваемого:", reply_markup=keyboard)


def register_finish_handlers(dp: Dispatcher):
    dp.message.register(finish_command, Command(commands=["finish"]))
