from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

start_admin_menu = [['Меню админа', 'Меню юзера']]
admin_menu = [['Рассылка'], ['Вернуться']]
start_two_row = [['Сделать запись ✍'], ['Аналитика 🧮', 'Информация ❓']]
analysis_two_row = [['Общая информация', 'Просмотр суммы'], ['Курсы валют', 'Подписка'], ['Вернуться']]
rates_menu = [['Курс на сегодня', 'Курс на дату'], ['Вернуться']]

choice_currency = [['USD', 'EUR'], ['RUB', 'BYN'], ['Вернуться']]
hide_choice_currency = [['#####', '#####'], ['#####', '#####'], ['Отмена ввода']]

myfin = [['Подробнее на myfin.by ', '', "https://myfin.by/currency/minsk"]]

delete_writes_inline = [['Удалить записи', 'delete_writes'], ['Отменить', 'cancel']]


def get_button_more_one_row(namekeys):
    """Созданно что бы было меньше кода при создании кнопок
    аргумент функции должен быть вида ['Кнопка1', 'Кнопка2']"""
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in namekeys:
        if len(i) == 1:
            btn1 = KeyboardButton(i[0])
            keys.add(btn1)
        elif len(i) == 2:
            btn2 = KeyboardButton(i[0])
            btn3 = KeyboardButton(i[1])
            keys.add(btn2, btn3)
        elif len(i) > 2:
            btn1 = KeyboardButton(i[0])
            btn2 = KeyboardButton(i[1])
            btn3 = KeyboardButton(i[2])
            keys.add(btn1, btn2, btn3)

    return keys


def get_inline_buttons(namekeys):
    """Созданно что бы было меньше кода при создании инлайн кнопок
    [0] -> text
    [1] ->callback_data
    [2] -> url
    пример 1: str = [['text_1', callback_data='callback_data_1'], ['text_2', callback_data='callback_data_2']] -> без url
    пример 2: str = [['text', '', 'url']] -> без callback_data"""
    inline_keys = InlineKeyboardMarkup()
    for i in namekeys:
        btn = InlineKeyboardButton("null")
        if len(i) >= 0:
            btn.text = i[0]
        if len(i) >= 1 and i[1] != '':
            btn.callback_data = i[1]
        if len(i) > 2:
            btn.url = i[2]
        inline_keys.insert(btn)
    return inline_keys
