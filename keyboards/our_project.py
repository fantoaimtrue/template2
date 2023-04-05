from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def our_project() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('🐢 Рептилии и черепахи', callback_data='project_1', url='https://t.me/secretsReptile')
        ],
        [
            InlineKeyboardButton('🐈 Домашние животные', callback_data='project_2', url='https://t.me/PetChatik')
        ],
        [
            InlineKeyboardButton('🌊 АкваЧатик', callback_data='project_2', url='https://t.me/AquaChatik')
        ],
    ])

    return ikb


def social() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('📲 Instagram', callback_data='instagram',
                                 url='https://instagram.com/zoo_zavr?igshid=YmMyMTA2M2Y=')
        ],
        [
            InlineKeyboardButton('📲 Вконтакте', callback_data='vk', url='https://vk.com/zoozavri')
        ]
    ])

    return ikb
