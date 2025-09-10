from aiogram import Router
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.fsm.state import State, StatesGroup
from keyboards.kb_users import *
import os

#сколько угодно админов
ADMIN_IDS = [
    int(v) for v in (
        os.getenv("ADM1_ID"),
        os.getenv("ADM2_ID"),
        os.getenv("ADM3_ID"),
    ) if v and v.isdigit()
]

users_router = Router()


@users_router.message(lambda message: message.text == '/start')
async def start_handler(message: types.Message, state: FSMContext):
    print('работает')
    print(f'{message.chat.id}')
    await state.clear()
    await message.answer('Все нужные ресурсы от бережного специалиста всегда под рукой. Для записи на консультацию нажмите на кнопку "Связаться со мной".', reply_markup = keyboard)


class Questions(StatesGroup):
    waiting_for_message = State()


@users_router.callback_query(lambda callback: callback.data == 'write_message')
async def write_message_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите ваш вопрос')
    await state.set_state(Questions.waiting_for_message)
    await callback.answer()


@users_router.message(Questions.waiting_for_message, lambda message: message.text)
async def catch_message(message: types.Message, state: FSMContext):
    user_text = message.text
    await state.update_data(msg=user_text)
    await message.answer(f'Ваш текст сообщения: \n\n <i>{user_text}</i>\n\n Отправить?', reply_markup = keyboard2, parse_mode = 'HTML')


@users_router.message(Questions.waiting_for_message)
async def text_only(message: types.Message):
    await message.answer('Пожалуйста, используйте только текст')


@users_router.callback_query(lambda callback: callback.data == 'canceled')
async def message_canceled(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await callback.message.edit_text(
            text = 'Все нужные ресурсы от бережного специалиста всегда под рукой. Для записи на консультацию нажмите на кнопку "Связаться со мной".',
            reply_markup = keyboard)
    except Exception:
        pass
    

@users_router.callback_query(lambda callback: callback.data == 'sent')
async def message_sent(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await callback.answer()
    print(data['msg'])
    try:
        user_info = f"{callback.from_user.full_name}\n"
        if callback.from_user.username:
            user_info += f"@{callback.from_user.username}\n"
        user_info += f"{callback.from_user.id}\n\n Сообщение:\n{data['msg']}"
        
        for admin_id in ADMIN_IDS:
            await callback.bot.send_message(admin_id, user_info)
        
        await callback.message.edit_text('Ваше сообщение отправлено. Совсем скоро я свяжусь с вами!', reply_markup = keyboard3)
    except Exception:
        pass


@users_router.callback_query(lambda callback: callback.data == 'backtostart')
async def message_sent2(callback: types.CallbackQuery):
    await callback.answer() 
    try:
        await callback.message.edit_text(
            text = 'Все нужные ресурсы от бережного специалиста всегда под рукой. Для записи на консультацию нажмите на кнопку "Связаться со мной".',
            reply_markup = keyboard)
    except Exception:
        pass