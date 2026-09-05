from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Главное меню пользователя
start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Перейти в канал",
                url="https://t.me/+9qxCzm9TvNVlOTky"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Я подписался",
                callback_data="start_application"
            )
        ]
    ]
)


# Главное меню администратора
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


# Кнопка "Назад" для администратора
admin_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="◀️ Назад",
                callback_data="admin_back"
            )
        ]
    ]
)
