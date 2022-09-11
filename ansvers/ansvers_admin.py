from aiogram import types
import loader

from models import Curs
from models.model_User import UserManager
from models.model_Money import Eur, Usd, Byn, Rub

from loader import bot
import keyboard


async def mailing(message: types.Message):
    if message.from_user.id == loader.admin:
        usd_rate = Curs.get_last_curs_usd()[0][0]
        eur_rate = Curs.get_last_curs_eur()[0][0]
        rub_rate = Curs.get_last_curs_rub()[0][0]
        for i in UserManager.get_list_subscribers():
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


async def information(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id == loader.admin:
            await message.answer("Приветствую Админа",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_admin_menu))
        else:
            await message.answer("Этот бот сделал Roman",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))
