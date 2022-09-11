import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext  # для машины состояний

import keyboard
from for_requests import nbrb
from for_states import Date_state
from models import Curs


async def menu_rates_currency(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Меню курс валют:", reply_markup=keyboard.get_button_more_one_row(keyboard.rates_menu))


async def get_curr_today(message: types.Message):
    rub = nbrb.get_rate_rub()
    eur = nbrb.get_rate_eur()
    usd = nbrb.get_rate_usd()
    curs = Curs(RUB=rub, USD=usd, EUR=eur)
    Curs.update_curs(curs)
    await message.answer(f"Курс по НБРБ на сегодня:\n\n"
                         f"RUB  :  {rub}\n"
                         f"USD  :  {usd}\n"
                         f"EUR  :  {eur}", reply_markup=keyboard.get_inline_buttons(keyboard.myfin))


#### сделать тут все что бы нормально работала, сейчас проблема с календарем
async def get_curs_on_date(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Введите дату: пример: " + str(datetime.date.today()))
        await Date_state.write_date_waiting.set()


async def write_date(message: types.Message, state: FSMContext, ):
    if message.chat.type == "private":
        run = True  ## первый пуск для проверки корректности даты
        run2 = ""  ## Этот run2 создан что бы не прошла дата будущая
        try:
            run2 = datetime.datetime.strptime(message.text, '%Y-%m-%d').date()
        except ValueError:
            run = False
        if run:
            if run2 < datetime.date.today():
                rub = nbrb.get_rate_rub(message.text)
                eur = nbrb.get_rate_eur(message.text)
                usd = nbrb.get_rate_usd(message.text)
                curs = Curs(RUB=rub, USD=usd, EUR=eur)
                Curs.update_curs(curs)
                await message.answer(f"Курс по НБРБ на сегодня:\n\n"
                                     f"RUB  :  {rub}\n"
                                     f"USD  :  {usd}\n"
                                     f"EUR  :  {eur}", reply_markup=keyboard.get_inline_buttons(keyboard.myfin))
            else:
                await message.answer("Мы не умеем делать прогноз курса)")
        else:
            await message.answer("Не верные данные")

    await state.finish()
