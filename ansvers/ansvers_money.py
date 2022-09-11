from aiogram import types
from aiogram.dispatcher import FSMContext  # для машины состояний

import keyboard
from for_states import Currency
from models.model_Money import Eur, Usd, Byn, Rub


async def menu_write_money(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        await state.finish()
        await message.answer("Меню записи валюты:",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.choice_currency))


async def start_write_byn(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Введите сумму в BYN, (на пример: 158,25 или 158):",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.hide_choice_currency))
        await Currency.write_byn_waiting.set()


async def write_byn(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        try:
            count_money = float(message.text)
        except ValueError:
            await message.answer("неверные данные, повторите попытку снова, или нажмите на кнопку 'Отмена ввода'")
            return
        await message.answer("Вы ввели: " + str(count_money) + " BYN",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.choice_currency))
        if Byn.add_money(message.from_user.id, count_money):
            await message.answer("Данные успешно сохранены")
        else:
            await message.answer("Ошибка сохранения в базу")
        await state.finish()


async def start_write_usd(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Введите сумму в USD, (на пример: 158,25 или 158):",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.hide_choice_currency))
        await Currency.write_usd_waiting.set()


async def write_usd(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        try:
            count_money = float(message.text)
        except ValueError:
            await message.answer("неверные данные, повторите попытку снова, или нажмите на кнопку 'Отмена ввода'")
            return
        await message.answer("Вы ввели: " + str(count_money) + " USD",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.choice_currency))
        if Usd.add_money(message.from_user.id, count_money):
            await message.answer("Данные успешно сохранены")
        else:
            await message.answer("Ошибка сохранения в базу")
        await state.finish()


async def start_write_eur(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Введите сумму в EUR, (на пример: 158,25 или 158):",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.hide_choice_currency))
        await Currency.write_eur_waiting.set()


async def write_eur(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        try:
            count_money = float(message.text)
        except ValueError:
            await message.answer("неверные данные, повторите попытку снова, или нажмите на кнопку 'Отмена ввода'")
            return
        await message.answer("Вы ввели: " + str(count_money) + " EUR",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.choice_currency))
        if Eur.add_money(message.from_user.id, count_money):
            await message.answer("Данные успешно сохранены")
        else:
            await message.answer("Ошибка сохранения в базу")
        await state.finish()


async def start_write_rub(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Введите сумму в RUB, (на пример: 1500.52 или 1500):",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.hide_choice_currency))
        await Currency.write_rub_waiting.set()


async def write_rub(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        try:
            count_money = float(message.text)
        except ValueError:
            await message.answer("неверные данные, повторите попытку снова, или нажмите на кнопку 'Отмена ввода'")
            return
        await message.answer("Вы ввели: " + str(count_money) + " RUB",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.choice_currency))
        if Rub.add_money(message.from_user.id, count_money):
            await message.answer("Данные успешно сохранены")
        else:
            await message.answer("Ошибка сохранения в базу")
        await state.finish()
