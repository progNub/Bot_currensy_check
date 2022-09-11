from aiogram import types
import loader
import keyboard


async def hello(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"Привет, {message.from_user.first_name}",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


async def main_menu(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Главное меню:",
                             reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


async def start(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id == loader.admin:
            await message.answer("Админ меню)",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_admin_menu))
        else:
            if UserManager.check_unique(message.from_user.id):
                if UserManager.add_new_user(message.from_user):
                    await message.answer("Ура, новый пользователь, Добро пожаловать)",
                                         reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))
                else:
                    await message.answer("Видимо бот еще не работает нормально)",
                                         reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))
            else:
                await message.answer("Добро пожаловать, " + message.from_user.first_name,
                                     reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))


async def information(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id == loader.admin:
            await message.answer("Приветствую Админа",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_admin_menu))
        else:
            await message.answer("Этот бот сделал Roman",
                                 reply_markup=keyboard.get_button_more_one_row(keyboard.start_two_row))
