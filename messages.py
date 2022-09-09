import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext  # для машины состояний
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback
import aioschedule, time, asyncio

import loader
from for_states import Currency, Date_state
from models import User, Curs, Byn, Usd, Eur, Rub
from for_requests import nbrb
from loader import bot
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
    curs = Curs(RUB=rub, USD=usd, EUR=eur)
    Curs.update_curs(curs)
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
        if message.from_user.id == loader.admin:
            await message.answer("Админ меню)",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_admin_menu))
        else:
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
        await message.answer("Главное меню:",
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
        usd = Usd.get_last_record(message.from_user.id)
        eur = Eur.get_last_record(message.from_user.id)
        rub = Rub.get_last_record(message.from_user.id)
        byn = Byn.get_last_record(message.from_user.id)
        sum_usd = usd * usd_rate
        sum_rub = (rub * rub_rate) / 100
        sum_eur = eur * eur_rate
        final_sum_byn = sum_eur + sum_rub + sum_usd + byn

        await message.answer("USD: {:<10.0f} курс {:>8.2f} BYN = {:>10.2f}\n".format(usd, usd_rate, sum_usd)
                             + "EUR: {:<10.0f} курс {:>8.2f} BYN = {:>10.2f}\n".format(eur, eur_rate, sum_eur)
                             + "RUB: {:<10.0f} курс {:>8.2f} BYN = {:>10.2f}\n".format(rub, rub_rate, sum_rub)
                             + "BYN: {:<10.0f}\n\n".format(byn)
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


async def menu_ubscribe(message: types.Message):
    if message.chat.type == "private":
        if User.check_subscribe(message.from_user.id):
            await message.answer(
                "Сделайте выбор.", reply_markup=keyboard.get_inline_buttons([['Отписаться', 'subscribe']]))
        else:
            await message.answer(
                "Сделайте выбор.", reply_markup=keyboard.get_inline_buttons([['Подписаться', 'subscribe']]))


async def subscribe(callback_query: types.CallbackQuery):
    if callback_query.message.chat.type == "private":
        User.subscribe(callback_query.from_user.id)
        if User.check_subscribe(callback_query.from_user.id):
            await callback_query.answer(
                "Вы подписались", cache_time=5)
        else:
            await callback_query.answer(
                "Вы отписались", cache_time=5)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


async def mailing(message: types.Message):
    if message.from_user.id == loader.admin:
        usd_rate = Curs.get_last_curs_usd()[0][0]
        eur_rate = Curs.get_last_curs_eur()[0][0]
        rub_rate = Curs.get_last_curs_rub()[0][0]
        for i in User.get_list_subscrubers():
            usd = Usd.get_last_record(i[0])
            eur = Eur.get_last_record(i[0])
            rub = Rub.get_last_record(i[0])
            byn = Byn.get_last_record(i[0])
            sum_usd = usd * usd_rate
            sum_rub = (rub * rub_rate) / 100
            sum_eur = eur * eur_rate
            final_sum_byn = sum_eur + sum_rub + sum_usd + byn
            await bot.send_message(chat_id=i[0],
                                   text="USD: {:<10.0f} курс {:>8.2f} BYN = {:>10.2f}\n".format(usd, usd_rate, sum_usd)
                                        + "EUR: {:<10.0f} курс {:>8.2f} BYN = {:>10.2f}\n".format(eur, eur_rate,
                                                                                                  sum_eur)
                                        + "RUB: {:<10.0f} курс {:>8.2f} BYN = {:>10.2f}\n".format(rub, rub_rate,
                                                                                                  sum_rub)
                                        + "BYN: {:<10.0f}\n\n".format(byn)
                                        + "Итоговая сумма в BYN: {:>.2f}".format(final_sum_byn))
        await bot.send_message(chat_id=loader.admin, text="Рассылка выполнена")


async def admin(message: types.message):
    if message.chat.type == "private":
        if loader.admin == message.from_user.id:
            await message.answer("Приветствую Админа",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.admin_menu))
