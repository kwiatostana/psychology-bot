from aiogram import types


keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Сайт', url='https://nadezhda-psychology.ru/'),
            types.InlineKeyboardButton(text='Тг-канал', url='https://t.me/tg_nadezhda_psychology')],
            [types.InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/@nadezhda-psyhology'),
            types.InlineKeyboardButton(text='Одноклассники', url='https://ok.ru/group/55477711208702')],
            [types.InlineKeyboardButton(text='Связаться со мной', callback_data='write_message')]
        ]
    )

keyboard2 = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Отправить', callback_data = 'sent'),
            types.InlineKeyboardButton(text='Отмена', callback_data = 'canceled')],
        ]
    )

keyboard3 = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Назад', callback_data = 'backtostart')],
        ]
    )