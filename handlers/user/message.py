import html

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from random import randint

from core.States import States
from keyboards.keyboard import start_menu as kb
from core.db import db
from core.config import Settings

router = Router()
settings = Settings()

async def start_handler(message: Message, state: FSMContext):
    await message.answer(f"Добрый день <b>{html.escape(message.from_user.first_name)}</b>! Оставьте заявку", 
                         reply_markup=kb)

async def reg_one(message: Message, state: FSMContext):
    await state.set_state(States.name)
    await message.answer("Введите ваше имя:")

async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(States.email)
    await message.answer("Введите вашу почту:")

async def reg_three(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(States.problem)
    await message.answer("Вашу проблему:")

async def reg_four(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)
    random_number = randint(1, 9999999)
    data = await state.get_data()
    await db.excute("INSERT INTO users (name, email, TEXT, number) VALUES (?, ?, ?, ?)", 
                    (data["name"], data["email"], data["problem"], random_number))
    await message.bot.send_message(chat_id=settings.ADMIN_ID[0],
                           text=f"Новая заявка:<code>{random_number}</code>\n\nИмя: {data['name']}\nПочта: {data['email']}\nПроблема: {data['problem']}")
    await message.answer(f"Спасибо!\nВаш номер заявки:<code>{random_number}</code>\nМы свяжемся с вами по указанному адресу.")
    await state.clear()


def register_handlers():
    router.message.register(start_handler, CommandStart())
    router.message.register(reg_one, F.text == "Оставить заявку")
    router.message.register(reg_two, States.name)
    router.message.register(reg_three, States.email)
    router.message.register(reg_four, States.problem)