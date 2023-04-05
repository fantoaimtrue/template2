from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def sale_inline() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('🌊 Все для аквариумов', callback_data='sale_aquarium')
        ],
        [
            InlineKeyboardButton('🐢 Черепахи и рептилии', callback_data='sale_reptiles')
        ],
        [
            InlineKeyboardButton('🐈 Кошки и собаки', callback_data='sale_pets')
        ],
    ])
    return ikb


# все для аквариумов
def sale_aquarium() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Фильтр на 60Л', callback_data='aqua_1'),
            InlineKeyboardButton('Набор скребков 5 в 1', callback_data='aqua_2')
        ],
        [
            InlineKeyboardButton('Автокормушка для рыб', callback_data='aqua_3'),
            InlineKeyboardButton('Автокормушка для рыб', callback_data='aqua_4')
        ],
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ])
    return ikb


# рептилии и черепахи
def sale_reptiles() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Плот для черепах ', callback_data='rept_1'),
            InlineKeyboardButton('Кормушка для рептилий', callback_data='rept_2')
        ],
        [
            InlineKeyboardButton('Кормушка для рептилий', callback_data='rept_3'),
            InlineKeyboardButton('Подсветка для бассейна', callback_data='rept_4')
        ],
        [
            InlineKeyboardButton('Генератор тумана', callback_data='rept_5'),
            InlineKeyboardButton('Гамак для рептилий', callback_data='rept_6')
        ],
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ])
    return ikb


# кошки и собаки
def sale_pets() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Уличная кормушка для птиц', callback_data='pets_1'),

        ],
        [
            InlineKeyboardButton('Ванночка для купания грызунов', callback_data='pets_2')
        ],
        [
            InlineKeyboardButton('Игрушка для дрессировки', callback_data='pets_3'),

        ],
        [
            InlineKeyboardButton('Электрическая когтеточка', callback_data='pets_4')
        ],
        [
            InlineKeyboardButton('Вольер для собак', callback_data='pets_5'),
        ],
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ])
    return ikb
