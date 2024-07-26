from aiogram import types, Dispatcher

from config import win, draw, lost
from db import show_hint_by_id

MAX_HINTS = 23

#hints = [f"Подсказка {i}" for i in range(1, MAX_HINTS + 1)]


async def process_callback_button(callback_query: types.CallbackQuery):
    data = callback_query.data.split("_")
    id = int(data[1])

    if data[0] != "suspected":
        hint = str(show_hint_by_id(id))
        await callback_query.message.answer(hint)
    else:
        if id == 2:
            result = draw
        elif id == 3:
            result = win
        else:
            result = lost

        await callback_query.message.answer(result)


def register_callback_handlers(dp: Dispatcher):
    dp.callback_query.register(
        process_callback_button, lambda c: c.data and (c.data.startswith("button") or c.data.startswith("suspected"))
    )