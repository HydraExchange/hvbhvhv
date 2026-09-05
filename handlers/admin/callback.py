import html

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from core.States import States
from keyboards.keyboard import admin_back as back
from keyboards.keyboard import admin_menu as kb
from core.db import db
from filters.check_admin import IsAdmin

router = Router()

async def requests(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Текущие заявки:\n{await db.get_requests()}", reply_markup=back)

async def admin_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Добрый день <b>{html.escape(callback.message.from_user.first_name)}</b>! Вы попали в админ-панель.", 
                         reply_markup=kb)

def register_handlers():
    router.callback_query.register(requests, F.data == "requests", IsAdmin())
    router.callback_query.register(admin_back, F.data == "back", IsAdmin())