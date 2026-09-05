from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from core.States import States


router = Router()


async def create_application(
    callback: CallbackQuery,
    state: FSMContext
):
    await callback.answer()

    await state.set_state(States.name)

    await callback.message.answer(
        "📝 <b>Создание заявки</b>\n\n"
        "Шаг 1 из 3\n\n"
        "👤 Введите ваш username Telegram в формате @юзер:"
    )


def register_handlers():
    # Кнопка "✅ Я подписался"
    router.callback_query.register(
        create_application,
        F.data == "start_application"
    )

    # Старая кнопка "📝 Оставить заявку"
    router.callback_query.register(
        create_application,
        F.data == "create_application"
    )
