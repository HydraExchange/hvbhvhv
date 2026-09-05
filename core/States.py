from aiogram.filters.state import StatesGroup, State


class States(StatesGroup):
    name = State()
    email = State()
    problem = State()
    user = State()
    admin = State()