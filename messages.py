from aiogram import types
from aiogram.dispatcher import FSMContext  # для машины состояний
from for_states import Currency
from models import User, Byn, Usd, Eur, Rub
from for_requests import get_rate
import keyboard

WELCOM = "Этот бот создан для облегчения ведения учета покупок валюты " \
         "он умеет хранить и обрабатывать информацию об этих покупках.\n" \
         "Сейчас доступно 3 валюты для записи: RUB, USD, EUR.\n\n"


async def analysis(message: types.Message):
    await message.answer("Меню аналитики 🧮", reply_markup=keyboard.get_button_more_one_row(keyboard.analysis_two_row))


async def get_curr(message: types.Message):
    rub = get_rate(456)
    eur = get_rate(451)
    usd = get_rate()
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
        if not (Byn.add_money(message.from_user.id, count_money)):
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
        if not (Usd.add_money(message.from_user.id, count_money)):
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
        if not (Eur.add_money(message.from_user.id, count_money)):
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
        if not (Rub.add_money(message.from_user.id, count_money)):
            await message.answer("Данные успешно сохранены")
        else:
            await message.answer("Ошибка сохранения в базу")
        await state.finish()
