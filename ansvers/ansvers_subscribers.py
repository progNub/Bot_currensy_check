from aiogram import types
import keyboard
from models.model_User import UserManager
from loader import bot


async def menu_subscribe(message: types.Message):
    if message.chat.type == "private":
        if UserManager.check_subscribe(message.from_user.id):
            await message.answer(
                "Сделайте выбор.", reply_markup=keyboard.get_inline_buttons([['Отписаться', 'subscribe']]))
        else:
            await message.answer(
                "Сделайте выбор.", reply_markup=keyboard.get_inline_buttons([['Подписаться', 'subscribe']]))


async def subscribe(callback_query: types.CallbackQuery):
    if callback_query.message.chat.type == "private":
        UserManager.subscribe(callback_query.from_user.id)
        if UserManager.check_subscribe(callback_query.from_user.id):
            await callback_query.answer(
                "Вы подписались", cache_time=5)
        else:
            await callback_query.answer(
                "Вы отписались", cache_time=5)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
