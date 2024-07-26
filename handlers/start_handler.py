from aiogram import types, Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from poetry.installation import executor
from config import history
from config import rules


async def rules_command(message: types.Message, start_game=None):
    BUTTONS_PER_ROW = 1
    # Создаем список кнопок для выбора истории или завершения
    # new_buttons =[
    #     [InlineKeyboardButton(
    #         text="Начать",
    #         callback_data=f"{start_game}"
    #     )]
    # ]
    #
    # new_keyboard = InlineKeyboardMarkup(
    #         type="inline", row_width=BUTTONS_PER_ROW, inline_keyboard=[*new_buttons]       # кнопка не переходит на нужую функцию
    #     )

    await message.reply(f"{rules} \n\n\nЧтобы начать нажмите на команду \n\n\n /start_game:  \n\n\n специально для Вас подготовлен арт \n\n\n /image") #, reply_markup=new_keyboard)


async def start_command(message: types.Message):
    BUTTONS_PER_ROW = 5
    MAX_BUTTONS = 23

    # Создаем список кнопок
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{row * BUTTONS_PER_ROW + col}",
                callback_data=f"button_{row * BUTTONS_PER_ROW + col}",
            )
            for col in range(1, BUTTONS_PER_ROW + 1)
        ]

        for row in range(0, MAX_BUTTONS // BUTTONS_PER_ROW + 1)


    ]

    # Обрезаем кнопки, если они больше максимального количества
    buttons[MAX_BUTTONS // BUTTONS_PER_ROW] = buttons[MAX_BUTTONS // BUTTONS_PER_ROW][
                                              :
                                              MAX_BUTTONS % BUTTONS_PER_ROW
                                              ]

    keyboard = InlineKeyboardMarkup(
            type="inline", row_width=BUTTONS_PER_ROW, inline_keyboard=[*buttons]
        )

    await message.reply(f"{history} \n\n\nВыберите 10 подсказок:", reply_markup=keyboard)

def register_start_handlers(dp: Dispatcher):
    dp.message.register(rules_command, Command(commands=["rules"]))
    dp.message.register(rules_command, Command(commands=["start"]))
    dp.message.register(start_command, Command(commands=["start_game"]))






