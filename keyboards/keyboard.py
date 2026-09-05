from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Кнопка для пользователя
start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📝 Оставить заявку",
                callback_data="create_application"
            )
        ]
    ]
)


# Клавиатура администратора
# Названия callback_data должны соответствовать обработчикам
# Если у тебя в admin/callback.py используются другие значения,
# их потом подгоним.
admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📋 Заявки",
                callback_data="applications"
            )
        ]
    ]
)
