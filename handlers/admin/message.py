import html

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from core.States import States
from keyboards.keyboard import admin_menu as kb
from core.db import db
from filters.check_admin import IsAdmin

router = Router()

async def admin_menu(message: Message, state: FSMContext):
    await message.answer(f"Добрый день <b>{html.escape(message.from_user.first_name)}</b>! Вы попали в админ-панель.", 
                         reply_markup=kb)

async def delete_request(message: Message, state: FSMContext, command: Command):
    if command.args:
        await db.excute("DELETE FROM users WHERE number = ?", (command.args,))

async def get_request(message: Message, state: FSMContext, command: Command):
    if command.args:
        await message.answer(await db.get_request(command.args))
def register_handlers():
    router.message.register(admin_menu, Command("admin"), IsAdmin())
    router.message.register(delete_request, Command("delete"), IsAdmin())
    router.message.register(get_request, Command("get"), IsAdmin())