import aiogram
from aiogram import executor
from aiogram.utils.exceptions import BotBlocked  # для ошибок телеги
from aiogram.utils import exceptions
from ansvers import ansvers_admin, ansvers_analitics, ansvers_subscribers, ansvers_money, ansvers_rates, \
    ansvers_default_commands
from aiogram.dispatcher.filters import Command
from for_states import Currency, Date_state

from loader import dp

dp.register_message_handler(ansvers_default_commands.start, Command('start'))

# админ
dp.register_message_handler(callback=ansvers_admin.information, regexp='Информация ❓')
dp.register_message_handler(callback=ansvers_admin.admin, regexp='Меню админа')
dp.register_message_handler(callback=ansvers_admin.mailing, regexp='Рассылка')

dp.register_message_handler(callback=ansvers_default_commands.main_menu, regexp='Меню юзера')

# Операции с валютой
dp.register_message_handler(callback=ansvers_money.menu_write_money, regexp='Сделать запись ✍')
dp.register_message_handler(callback=ansvers_money.menu_write_money, regexp='Отмена ввода', state="*")
dp.register_message_handler(callback=ansvers_money.start_write_byn, regexp='BYN')
dp.register_message_handler(callback=ansvers_money.start_write_usd, regexp='USD')
dp.register_message_handler(callback=ansvers_money.start_write_eur, regexp='EUR')
dp.register_message_handler(callback=ansvers_money.start_write_rub, regexp='RUB')
dp.register_message_handler(callback=ansvers_money.write_byn, state=Currency.write_byn_waiting)
dp.register_message_handler(callback=ansvers_money.write_usd, state=Currency.write_usd_waiting)
dp.register_message_handler(callback=ansvers_money.write_eur, state=Currency.write_eur_waiting)
dp.register_message_handler(callback=ansvers_money.write_rub, state=Currency.write_rub_waiting)

# Меню аналитики
dp.register_message_handler(callback=ansvers_analitics.analysis, regexp='Аналитика 🧮')
dp.register_message_handler(callback=ansvers_default_commands.main_menu, regexp='Вернуться')

dp.register_message_handler(callback=ansvers_subscribers.menu_subscribe, regexp='Подписка')
dp.register_callback_query_handler(callback=ansvers_subscribers.subscribe)

dp.register_message_handler(callback=ansvers_analitics.get_all_currency, regexp='Общая информация')
dp.register_message_handler(callback=ansvers_analitics.get_sum_all_currency, regexp='Просмотр суммы')

dp.register_message_handler(callback=ansvers_rates.menu_rates_currency, regexp='Курсы валют')
dp.register_message_handler(callback=ansvers_rates.get_curr_today, regexp='Курс на сегодня')
dp.register_message_handler(callback=ansvers_rates.get_curs_on_date, regexp='Курс на дату')
dp.register_message_handler(callback=ansvers_rates.write_date, state=Date_state.write_date_waiting)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print("Бот запущен"))
