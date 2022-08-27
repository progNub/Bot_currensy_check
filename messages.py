from aiogram import types
from aiogram.dispatcher import FSMContext  # для машины состояний
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback
from for_states import Currency
from models import User, Curs, Byn, Usd, Eur, Rub
from for_requests import nbrb
import keyboard

WELCOM = "Этот бот создан для облегчения ведения учета покупок валюты " \
         "он умеет хранить и обрабатывать информацию об этих покупках.\n" \
         "Сейчас доступно 3 валюты для записи: RUB, USD, EUR.\n\n"


async def analysis(message: types.Message):
    await message.answer("Меню аналитики 🧮", reply_markup=keyboard.get_button_more_one_row(keyboard.analysis_two_row))


async def get_curr_today(message: types.Message):
    rub = nbrb.get_rate_rub()
    eur = nbrb.get_rate_eur()
    usd = nbrb.get_rate_usd()
    await message.answer(f"Курс по НБРБ на сегодня:\n\n"
                         f"RUB  :  {rub}\n"
                         f"USD  :  {usd}\n"
                         f"EUR  :  {eur}", reply_markup=keyboard.get_inline_buttons(keyboard.myfin))


async def hello(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"Привет, {message.from_user.first_name}",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


async def start(message: types.Message):
    if message.chat.type == "private":
        if User.check_unique(message.from_user.id):
            if User.add_new_user(message.from_user):
                await message.answer("Ура, новый пользователь, Добро пожаловать)",
                                     reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))
            else:
                await message.answer("Видимо бот еще не работает нормально)",
                                     reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))
        else:
            await message.answer("Добро пожаловать, " + message.from_user.first_name,
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


async def main_menu(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Возврат в главное меню:",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


async def information(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Этот бот сделал Roman",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


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


async def get_sum_all_currency(message: types.Message):
    if message.chat.type == "private":
        usd_rate = Curs.get_last_curs_usd()[0][0]
        eur_rate = Curs.get_last_curs_eur()[0][0]
        rub_rate = Curs.get_last_curs_rub()[0][0]

        usd = Usd.get_last_record(message.from_user.id)[0][0]
        eur = Eur.get_last_record(message.from_user.id)[0][0]
        rub = Rub.get_last_record(message.from_user.id)[0][0]
        byn = Byn.get_last_record(message.from_user.id)[0][0]

        sum_usd = usd * usd_rate
        sum_rub = (rub * rub_rate) / 100
        sum_eur = eur * eur_rate

        final_sum_byn = sum_eur + sum_rub + sum_usd + byn
        "Куплено: EUR = {:>.2f}\n".format(eur)
        await message.answer("Сумма USD в BYN: {:>.2f}\n".format(sum_usd)
                             + "Сумма EUR в BYN: {:>.2f}\n".format(sum_eur)
                             + "Сумма RUB в BYN: {:>.2f}\n".format(sum_rub)
                             + "Сумма BYN: {:>.2f}\n\n".format(byn)
                             + "Итоговая сумма в BYN: {:>.2f}".format(final_sum_byn))


async def get_all_currency(message: types.Message):
    if message.chat.type == "private":
        usd = Usd.get_last_record(message.from_user.id)
        eur = Eur.get_last_record(message.from_user.id)
        rub = Rub.get_last_record(message.from_user.id)
        byn = Byn.get_last_record(message.from_user.id)
        await message.answer(f"BYN: {byn[0][0]}\nUSD: {usd[0][0]}\nEUR: {eur[0][0]}\nRUB: {rub[0][0]}")


async def menu_rates_currency(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Меню курс валют:", reply_markup=keyboard.get_button_more_one_row(keyboard.rates_menu))


async def get_curs_on_date(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Введите дату:")
