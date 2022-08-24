import asyncio

from aiogram import types
from aiogram.utils.exceptions import BotBlocked  # для ошибок телеги
from aiogram.dispatcher import FSMContext  # для машины состояний

import for_request

import keyboard
from keyboard import start_two_row, analysis_two_row, currency_two_row, currency_two_row_state_2, delete_writes_inline, \
    myfin

WELCOM = "Этот бот создан для облегчения ведения учета покупок валюты " \
         "он умеет хранить и обрабатывать информацию об этих покупках.\n" \
         "Сейчас доступно 3 валюты для записи: RUB, USD, EUR.\n\n"


async def analysis(message: types.Message):
    await message.answer("Меню аналитики 🧮", reply_markup=keyboard.get_button_more_one_row(analysis_two_row))


async def get_curr(message: types.Message):
    rub = for_request.get_rate(456)
    eur = for_request.get_rate(451)
    usd = for_request.get_rate()
    await message.answer(f"Курс по НБРБ на сегодня:\n\n"
                         f"RUB  :  {rub}\n"
                         f"USD  :  {usd}\n"
                         f"EUR  :  {eur}", reply_markup=keyboard.get_inline_buttons(myfin))


async def hello(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"Привет, {message.from_user.first_name}",
                             reply_markup=keyboard.get_button_more_one_row(start_two_row))


async def start(message: types.Message):
    if message.chat.type == "private":
        await message.answer("start", reply_markup=keyboard.get_button_more_one_row(start_two_row))


async def main_menu(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Возврат в главное меню:", reply_markup=keyboard.get_button_more_one_row(start_two_row))


async def information(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Этот бот сделал Roman", reply_markup=keyboard.get_button_more_one_row(start_two_row))


async def write_money(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Меню записи денег:", reply_markup=keyboard.get_button_more_one_row(currency_two_row))


