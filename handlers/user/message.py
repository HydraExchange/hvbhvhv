import html
from random import randint

from aiogram import Router, F
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
        f"👋 Добрый день, <b>{name}</b>!\n\n"
        "Добро пожаловать в <b>LIBERTY ЗАЯВКИ</b>.\n\n"
        "Здесь вы можете оставить заявку. "
        "Для этого нажмите кнопку ниже 👇",
        reply_markup=kb,
    )


async def reg_one(message: Message, state: FSMContext):
    await state.set_state(States.name)
    await message.answer(
        "📝 <b>Создание заявки</b>\n\n"
        "Шаг 1 из 3\n\n"
        "Введите ваше имя:"
    )


async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(States.email)

    await message.answer(
        "📧 <b>Шаг 2 из 3</b>\n\n"
        "Введите вашу электронную почту:"
    )


async def reg_three(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(States.problem)

    await message.answer(
        "📋 <b>Шаг 3 из 3</b>\n\n"
        "Опишите вашу проблему или вопрос:"
    )


async def reg_four(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)

    data = await state.get_data()
    random_number = randint(1000000, 9999999)

    await db.execute(
        "INSERT INTO users (name, email, TEXT, number) VALUES (?, ?, ?, ?)",
        (
            data["name"],
            data["email"],
            data["problem"],
            random_number,
        ),
    )

    await message.bot.send_message(
        chat_id=settings.ADMIN_ID,
        text=(
            "🔔 <b>Новая заявка!</b>\n\n"
            f"🆔 Номер: <code>{random_number}</code>\n"
            f"👤 Имя: {html.escape(data['name'])}\n"
            f"📧 Почта: {html.escape(data['email'])}\n"
            f"📋 Проблема: {html.escape(data['problem'])}"
        ),
    )

    await message.answer(
        "✅ <b>Заявка успешно отправлена!</b>\n\n"
        f"Номер вашей заявки: <code>{random_number}</code>\n\n"
        "Мы получили вашу заявку и свяжемся с вами по указанному адресу."
    )

    await state.clear()


def register_handlers():
    router.message.register(start_handler, CommandStart())
    router.message.register(reg_one, F.text == "Оставить заявку")
    router.message.register(reg_two, States.name)
    router.message.register(reg_three, States.email)
    router.message.register(reg_four, States.problem)
