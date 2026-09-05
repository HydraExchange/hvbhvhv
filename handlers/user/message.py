import html
from random import randint

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.States import States
from core.config import Settings
from core.db import db
from keyboards.keyboard import start_menu as kb


router = Router()
settings = Settings()


async def start_handler(message: Message, state: FSMContext):
    await state.clear()

    name = html.escape(message.from_user.first_name or "пользователь")

    await message.answer(
        f"👋 Добро пожаловать в <b>LIBERTY TEAM!</b>, {name}!\n\n"
        "Для начала работы необходимо заполнить заявку.\n\n"
        "Отвечайте на вопросы максимально детально и правдиво.\n"
        "⚠️ Ленивые и неполные заявки будут отклонены.\n\n"
        "Если готовы начать — нажмите кнопку ниже 👇",
        reply_markup=kb
    )


async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(States.email)

    await message.answer(
        "💰 <b>Какой депозит для работы с BTC у вас есть?</b>"
    )


async def reg_three(message: Message, state: FSMContext):
    await state.update_data(email=message.text)

    await state.set_state(States.problem)

    await message.answer(
        "📝 <b>Ответьте на вопросы одним сообщением и максимально детально.</b>\n\n"
        "1️⃣ 📢 <b>Откуда вы узнали о команде?</b>\n"
        "Отправьте ссылку на источник — обязательный шаг.\n\n"
        "2️⃣ ⏱️ <b>Сколько времени готовы уделять работе и почему мы должны выбрать именно вас?</b>"
    )

async def reg_four(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)

    data = await state.get_data()

    random_number = randint(1000000, 9999999)

    await db.excute(
        "INSERT INTO users (name, email, TEXT, number) VALUES (?, ?, ?, ?)",
        (
            data["name"],
            data["email"],
            data["problem"],
            random_number
        )
    )

    await message.bot.send_message(
        chat_id=settings.ADMIN_ID,
        text=(
            "🔔 <b>Новая заявка!</b>\n\n"
            f"🆔 Номер: <code>{random_number}</code>\n"
            f"👤 USER: {html.escape(data['name'])}\n"
            f"📧ДЕП: {html.escape(data['email'])}\n"
            f"📋ВОПРОСЫ {html.escape(data['problem'])}"
        )
    )

    await message.answer(
        "✅ <b>Заявка успешно отправлена!</b>\n\n"
        f"Номер вашей заявки: <code>{random_number}</code>\n\n"
        "Мы получили вашу заявку и свяжемся с вами."
    )

    await state.clear()


def register_handlers():
    router.message.register(
        start_handler,
        CommandStart()
    )

    router.message.register(
        reg_two,
        States.name
    )

    router.message.register(
        reg_three,
        States.email
    )

    router.message.register(
        reg_four,
        States.problem
    )
