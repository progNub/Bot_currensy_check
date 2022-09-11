from aiogram import types

import keyboard
from models import Curs
from models.model_Money import Eur, Usd, Byn, Rub


async def analysis(message: types.Message):
    await message.answer("Меню аналитики 🧮", reply_markup=keyboard.get_button_more_one_row(keyboard.analysis_two_row))

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
        await message.answer(f"BYN: {byn}\nUSD: {usd}\nEUR: {eur}\nRUB: {rub}")
