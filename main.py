import aiogram
from aiogram import executor
from aiogram.utils.exceptions import BotBlocked  # для ошибок телеги
from aiogram.utils import exceptions
from aiogram.dispatcher.filters import Command
from for_states import Currency
import messages
from loader import dp

dp.register_message_handler(messages.start, Command('start'))

#Операции с валютой
dp.register_message_handler(messages.menu_write_money, regexp='Сделать запись ✍')
dp.register_message_handler(messages.menu_write_money, regexp='Отмена ввода', state="*")
dp.register_message_handler(messages.start_write_byn, regexp='BYN')
dp.register_message_handler(messages.start_write_usd, regexp='USD')
dp.register_message_handler(messages.start_write_eur, regexp='EUR')
dp.register_message_handler(messages.start_write_rub, regexp='RUB')
dp.register_message_handler(messages.write_byn, state=Currency.write_byn_waiting)
dp.register_message_handler(messages.write_usd, state=Currency.write_usd_waiting)
dp.register_message_handler(messages.write_eur, state=Currency.write_eur_waiting)
dp.register_message_handler(messages.write_rub, state=Currency.write_rub_waiting)

#Меню аналитики
dp.register_message_handler(messages.analysis, regexp='Аналитика 🧮')
dp.register_message_handler(messages.main_menu, regexp='Вернуться')

dp.register_message_handler(messages.get_all_currency, regexp='Общая информация')
dp.register_message_handler(messages.get_sum_all_currency, regexp='Просмотр суммы')
dp.register_message_handler(messages.menu_rates_currency, regexp='Курсы валют')
dp.register_message_handler(messages.get_curr_today, regexp='Курс на сегодня')



dp.register_message_handler(messages.information, regexp='Информация ❓')

# currency



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print("Бот запущен"))
