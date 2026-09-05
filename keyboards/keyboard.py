from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оставить заявку")
        ]
    ], resize_keyboard=True
)
admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Заявки", callback_data="requests"),
            InlineKeyboardButton(text="Заявка", callback_data="request")
        ]
    ]
)
admin_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)