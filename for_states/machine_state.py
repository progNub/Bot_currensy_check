from aiogram.utils.helper import Helper, HelperMode
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp


class Currency(StatesGroup):
    write_byn_waiting = State()
    write_usd_waiting = State()
    write_eur_waiting = State()
    write_rub_waiting = State()


class Analitics(StatesGroup):
    state_1 = State()
