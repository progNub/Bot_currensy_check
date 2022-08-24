from aiogram import executor
from aiogram.utils.exceptions import BotBlocked  # для ошибок телеги
from aiogram.utils import exceptions
from aiogram.dispatcher.filters import Command
from for_states import Currency, Analitics

import messages
from loader import dp

dp.register_message_handler(messages.start, Command('start'))

# dp.register_callback_query_handler(messages.delete_writes, lambda c: c.data == 'delete_writes')
# dp.register_callback_query_handler(messages.cancel_delete, lambda c: c.data == 'cancel')


dp.register_message_handler(messages.write_money, regexp='Сделать запись ✍')
dp.register_message_handler(messages.analysis, regexp='Аналитика 🧮')
dp.register_message_handler(messages.information, regexp='Информация ❓')

# currency
dp.register_message_handler(messages.main_menu, regexp='Вернуться')
# dp.register_message_handler(messages.write_byn, regexp='BYN')
# dp.register_message_handler(messages.write_usd, regexp='USD')
# dp.register_message_handler(messages.write_eur, regexp='EUR')
# dp.register_message_handler(messages.write_rub, regexp='RUB')


dp.register_message_handler(messages.get_curr, regexp='Курсы валют')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print("Бот запущен"))
