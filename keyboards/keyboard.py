from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📝ПОДАТЬ ЗАЯВКУ",
                callback_data="create_application"
            )
        ]
    ]
)
