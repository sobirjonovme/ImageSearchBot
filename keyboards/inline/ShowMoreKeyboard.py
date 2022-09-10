

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import show_callback


async def generate_button(name, idx):

    show_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Show more", 
                    callback_data=show_callback.new(
                        item_name=name,
                        index=idx
                    )
                )
            ]
        ]
    )

    return show_button