from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from core.States import States

router = Router()

async def start_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите ваше имя:")
    
def register_handlers():
    router.callback_query.register(start_handler, F.data == "Help")
    