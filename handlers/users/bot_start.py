from aiogram import types
from loader import dp
from loader import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from filters import IsPrivate
from filters import IsGroup
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit
from keyboards.main_menu import get_reply_keyboard
from keyboards.our_project import our_project, social
from aiogram.utils.markdown import hlink
from keyboards.sale_inline import sale_inline
from keyboards.sale_inline import sale_aquarium
from keyboards.sale_inline import sale_reptiles
from keyboards.sale_inline import sale_pets
from loader import logging


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text=['/start'])
async def command_start(message: types.Message):
    try:
        user = await commands.select_users(message.from_user.id)
        if user.status == 'active':
            await message.answer('Ты уже зарегистрирован', reply_markup=get_reply_keyboard())
            text = f"Приветствует вас в нашем Telegram-боте помощнике <b>Секреты Хамелеона</b>👋\n\n<b>Здесь вы можете</b>\n\n-Найти все ваши Telegram чаты и Соц.сети\n-Ознакомиться с правилами чатов\n-Нашей продукцией для животных (зоотовары)"

            text_2 = "Наши чаты:"
            text_3 = "Наши социальные сети:"

            await bot.send_message(chat_id=message.from_user.id, text=f'{text}')

            await bot.send_message(chat_id=message.from_user.id, text=f'<b>{text_2}</b>', reply_markup=our_project())

            await bot.send_message(chat_id=message.from_user.id, text=f'<b>{text_3}</b>', reply_markup=social())

            await message.delete()
        elif user.status == 'ban':
            await message.answer("Ты забанен!")
    except Exception:
        await message.answer('Ты успешно зарегистрирован!', reply_markup=get_reply_keyboard())
        await commands.add_user(user_id=message.from_user.id, first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name, username=message.from_user.username,
                                status='active')
        text = f"Приветствует вас в нашем Telegram-боте помощнике 'Секреты Хамелеона'👋\n\n<b>Здесь вы можете</b>\n\n-Найти все ваши Telegram чаты и Соц.сети\n-Ознакомиться с правилами чатов\n-Нашей продукцией для животных (зоотовары)"

        text_2 = "Наши чаты"
        text_3 = "Наши социальные сети:"

        await bot.send_message(chat_id=message.from_user.id, text=f'{text}')

        await bot.send_message(chat_id=message.from_user.id, text=f'<b>{text_2}</b>', reply_markup=our_project())

        await bot.send_message(chat_id=message.from_user.id, text=f'<b>{text_3}</b>', reply_markup=social())

        await message.delete()


### Правила ###
@rate_limit(3)
@dp.message_handler(IsPrivate(), text='Правила чата')
async def chat_rules(message: types.Message) -> None:
    link = hlink('магазине', 'https://ozon.ru/t/W30VoyJ')
    text = f"✅Поддерживайте доброжелательную атмосферу - воздержитесь от мата, оскорблений.\n\n✅Вы вольны обсуждать в чате все что социально приемлемо и не несет пропаганды тематик 18+.\n\n✅Запрещается любая реклама не согласованная с администратором сообщества.\n\n✅Все ссылки, анонсы, информация о продаже чего-либо - должны быть согласованы с администратором. Возможны условия сотрудничества.\n\n ✅Любой спам и нарушение правил будет караться временным или постоянным баном.\n\n⭐️ У нас действует рейтинговая система.\nДля того что бы повысить рейтинг, нужно ответить на сообщение фразой <b>'+rep'</b>(если понизить <b>'-rep'</b>)\n\n🙏 Так же если вам понравился ответ вы можете отблагодарить, сказав одну из следующих фраз: (<b>'спс'</b>,<b>'благодарю'</b>,<b>'спасибо'</b>) в ответ на сообщение пользователя который вам помог. В будущем исходя из рейтинга мы будем разыгровать призы, а так же делать выгодные скидки в нашем {link} "
    await bot.send_message(chat_id=message.from_user.id, text=f'{text}')

    await message.delete()


### Наши продукты ###
@rate_limit(3)
@dp.message_handler(IsPrivate(), text='Наши ЗооТовары')
async def our_products(message: types.Message) -> None:
    link = hlink('магазин', 'https://ozon.ru/t/W30VoyJ')
    text = f"<b>ЗооТовары</b>\nПерейти в {link}"
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{text}\n\nили выберите раздел продукции что вас интересует тут',
                           reply_markup=sale_inline())
    await message.delete()


# === Все для аквариумов
@dp.callback_query_handler(text='sale_aquarium')
async def aqua_menu(callback: types.CallbackQuery):
    if callback.data == 'sale_aquarium':
        await callback.message.answer('Все для аквариумов', reply_markup=sale_aquarium())
    await callback.answer()


# Фильтр для небольшого аквариума до 60Л
@dp.callback_query_handler(text='aqua_1')
async def sale_aqua_1(callback: types.CallbackQuery):
    try:
        if callback.data == 'aqua_1':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/nk18AdA')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-s/wc1000/6425026468.jpg'
            caption = f'<b>Фильтр для небольшого аквариума до 60Л</b>\n\nВнутренний фильтр в аквариум размером 18см в высоту и диаметром 7см камерного типа с функцией аэрации создан для очищения и насыщения кислородом пресной или соленой воды. Фильтр предназначен для аквариумов объемом от 50 до 100 литров. \n\n<b>Комплектация</b>\n1. Фильр - 1 шт\n2. Насадка для изменения направление потока воды - 1 шт.\n3. Переходник для обеспечения перехода между разнотипными розетками - 1 шт.\n4. Силиконовая трубка 50см с насадкой - 1шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Набор инструментов для чистики и ухода за аквариумом 5 в 1: скребки для аквариума
@dp.callback_query_handler(text='aqua_2')
async def sale_aqua_2(callback: types.CallbackQuery):
    try:
        if callback.data == 'aqua_2':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/YbLR69o')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-h/wc1000/6387482777.jpg'
            caption = f'<b>Набор инструментов для чистики и ухода за аквариумом 5 в 1</b>\n\nНабор аксессуаров для ухода за аквариумом 5 в 1 - это Ваш незаменимый помощник для содержания аквариума в чистоте. Насадки выполнены из качественного и безопасного пластика. В набор для аквариума входят необходимые инструменты для ухода за рыбками, черепахами и улитками.\n\n<b>Комплектация</b>\n1. Ручка с рукояткой\n2. Держатель для насадок.\n3. Сачок.\n4. Скребок металлический.\n5. Скребок-губка.\n6. Грабли для грунта.\n7. Вилка для оформления декора'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Автоматическая кормушка для рыб в аквариум или террариум с таймером
@dp.callback_query_handler(text='aqua_3')
async def sale_aqua_3(callback: types.CallbackQuery):
    try:
        if callback.data == 'aqua_3':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/Awl3JYK')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-7/wc1000/6422339083.jpg'
            caption = f'<b>Автоматическая кормушка для рыб в аквариум или террариум с таймером</b>\n\nАвтокормушка черно-синяя для рыб и рептилий - ваш помощник в уходе за любимцами. Регулярное кормление аквариумных обитателей – залог их хорошего самочувствия и активного роста. Автоматическая кормушка для рыб, черепах или рептилий, покормит питомцев за вас через выбранным промежуток времени. \n\n<b>Комплектация</b>\n1. Автокормушка - 1 шт.\n2. Сменная емкость для корма 50г - 1 шт.\n3. Сменная емкость для корма 100г - 1 шт.\n4. Кронштейн - 1шт.\n5. Клейкая липучка - 1 шт. \n6. Батарейка пальчиковая - 2шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Автоматическая кормушка AF-2009D для рыб в аквариум или террариум с таймером. Автокормушка с разными режимами работы, черного цвета.
@dp.callback_query_handler(text='aqua_4')
async def sale_aqua_4(callback: types.CallbackQuery):
    try:
        if callback.data == 'aqua_4':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/MKXER27')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-y/wc1000/6473854534.jpg'
            caption = f'<b>Автоматическая кормушка для рыб в аквариум или террариум с таймером</b>\n\nАвтокормушка черно-синяя для рыб и рептилий - ваш помощник в уходе за любимцами. Регулярное кормление аквариумных обитателей – залог их хорошего самочувствия и активного роста. Автоматическая кормушка для рыб, черепах или рептилий, покормит питомцев за вас через выбранным промежуток времени. \n\n<b>Комплектация</b>\n1. Автокормушка - 1 шт.\n2. Сменная емкость для корма 50г - 1 шт.\n3. Сменная емкость для корма 100г - 1 шт.\n4. Кронштейн - 1шт.\n5. Клейкая липучка - 1 шт. \n6. Батарейка пальчиковая - 2шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')

    await callback.answer()


# === Черепахи и рептилии
@dp.callback_query_handler(text='sale_reptiles')
async def rept_menu(callback: types.CallbackQuery):
    if callback.data == 'sale_reptiles':
        await callback.message.answer('Черепахи и рептилии', reply_markup=sale_reptiles())
    await callback.answer()


# Плот для черепах пластиковый на присосках в аквариум или террариум
@dp.callback_query_handler(text='rept_1')
async def sale_rept_1(callback: types.CallbackQuery):
    try:
        if callback.data == 'rept_1':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/W39wG6n')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-w/wc1000/6392713556.jpg'
            caption = f'<b>Плот для черепах пластиковый на присосках в аквариум или террариум, крепится на стенку</b>\n\nПлот для водной черепахи размером 18*12*4см из пластика с искусственным покрытием в виде травы на присосках. Черепахам необходим атмосферный воздух и теплый участок суши, где можно хорошо погреться, просушить панцирь и отдохнуть, поэтому в вашем аквариуме обязательно должен быть плотик или островок, занимающий четвертую часть аквариума. Более точно вы сможете подобрать размер суши, измерив ваше животное. В длину плот должен вмещать 2-3 длины черепахи и быть в 2 раза шире вашего питомца.\n\n<b>Комплектация</b>\n1. Плот для черепахи - 1шт;\n2. Присоска - 2шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Кормушка поилка на присоске для ящериц, хамелеонов, гекконов, игуан и других рептилий в аквариум или террариум.
@dp.callback_query_handler(text='rept_2')
async def sale_rept_2(callback: types.CallbackQuery):
    try:
        if callback.data == 'rept_2':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/3eERnwr')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-d/wc1000/6433540633.jpg'
            caption = f'<b>Кормушка поилка на присоске для ящериц, хамелеонов, гекконов, игуан и других рептилий в аквариум или террариум.</b>\n\nКормушка поилка для ящериц, хамелеонов, гекконов и других рептилий - обязательный элементы домашнего террариума или аквариума, где содержатся рептилии. Этим экзотичным питомцам, как и всем живым существам на земле, для здоровой и долгой жизни необходимо питание и питьевая жидкость.\n\n<b>Комплектация</b>\nКормушка-поилка - 1шт.\n2. Присоска на кронштейне - 1 шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Кормушка на присосках для ящериц, хамелеонов, гекконов и игуан. Поилка для рептилий в аквариум или террариум.
@dp.callback_query_handler(text='rept_3')
async def sale_rept_3(callback: types.CallbackQuery):
    try:
        if callback.data == 'rept_3':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/bB7p4Vo')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-0/wc1000/6433689948.jpg'
            caption = f'<b>Кормушка на присосках для ящериц, хамелеонов, гекконов и игуан</b>\n\nКормушка поилка для ящериц, хамелеонов, гекконов и других рептилий - обязательный элементы домашнего террариума или аквариума, где содержатся рептилии. Этим экзотичным питомцам, как и всем живым существам на земле, для здоровой и долгой жизни необходимо питание и питьевая жидкость.\n\n<b>Комплектация</b>\nКормушка-поилка - 1шт.\n2. Присоска - 2 шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Светодиодная подсветка для бассейна, аквариума и террариума
@dp.callback_query_handler(text='rept_4')
async def sale_rept_4(callback: types.CallbackQuery):
    try:
        if callback.data == 'rept_4':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/dB8nwGl')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-5/wc1000/6480244001.jpg'
            caption = f'<b>Светодиодная подсветка для бассейна, аквариума и террариума.</b>\n\nДекоративная светодиодная подсветка состоит из 13 светодиодов, свет которых можно менять по 16 цветам, это позволяет создать комфортное обитание вашим аквариумным питомцам, вне зависимости от вашего региона проживания. Декоративный светодиодный подводный RGB-светильник не зависит от сети, работает от 3 батареек типа ААА (не входят в комплект), подсветку можно погружать на глубину до 6 метров.\n\n<b>Комплектация</b>\n1. Светодиодная подсветка - 1 шт.\n2. Дистанционный пульт управления - 1шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Туманогенератор для рептилий и хамелеонов. Генератор тумана в террариум, объём 4 литра.
@dp.callback_query_handler(text='rept_5')
async def sale_rept_5(callback: types.CallbackQuery):
    try:
        if callback.data == 'rept_5':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/geZ34nz')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-6/wc1000/6499307118.jpg'
            caption = f'<b>Туманогенератор для рептилий и хамелеонов</b>\n\nТуманогенератор для террариума создает и поддерживает уровень влажности. Это внешнее устройство, которое обеспечивает туман в джунглях террариума или тропического террариума. Ультразвуковой туманогенератор для небольших террариумов создает очень тонкий и обильный туман. Для большинства рептилий крайне важно поддерживать определенный уровень влажности, соответствующий показателям естественной среды их обитания. Не соблюдение условий содержания может привести к различным неблагоприятным последствиям.\n\n<b>Комплектация</b>\n1. Резервуар для воды.\n2. Генератор тумана.\n3. Шланг.\n4. Крепежи шланга.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Гамак для ящериц и рептилий на присосках.
@dp.callback_query_handler(text='rept_6')
async def sale_rept_6(callback: types.CallbackQuery):
    try:
        if callback.data == 'rept_6':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/XowLRyw')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-v/wc1000/6561373015.jpg'
            caption = f'<b>Гамак для ящериц и рептилий на присосках.</b>\n\nГамак для рептилий подходит для размещения в террариуме, универсален в применении. Может использоваться как место для сна и отдыха домашнего питомца, а также как место для игр. Благодаря простоте механизмов крепления, гамак можно расположить внутри террариума под разными углами, что позволяет обеспечить максимальный комфорт для вашего любимца. Совокупность высококачественных материалов и конструкции без сложных элементов, позволяют использовать гамак длительное время без замен и починки.\n\n<b>Комплектация</b>\n1. Гамак - 1шт;\n2. Присоска - 3шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except Exception as ex:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# === Кошки и собаки
@dp.callback_query_handler(text='sale_pets')
async def pets_menu(callback: types.CallbackQuery):
    if callback.data == 'sale_pets':
        await callback.message.answer('Товары для кошек и собак', reply_markup=sale_pets())
    await callback.answer()


# Уличная кормушка для птиц
@dp.callback_query_handler(text='pets_1')
async def sale_pets_1(callback: types.CallbackQuery):
    try:
        if callback.data == 'pets_1':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/bB7p4Vo')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-v/wc1000/6475614571.jpg'
            caption = f'<b>Прозрачная уличная кормушка для птиц на присосках с контейнером на окно.</b>\n\nПтицы являются прекраснейшими существами, которые вдохновляют человека, и становятся лучшими друзьями. Зимой кормушка для птиц просто необходима, поэтому многие люди хотят заказать товар именно в это время года. Однако такое решение не совсем верное, так как птицам кормушка нужна в любое время года. Задумывались ли вы, что одна кормушка, повешенная за окно или на дерево, обеспечивает пропитанием несколько сотен птиц.\n\n<b>Комплектация</b>\n1. Кормушка для птиц - 1 шт;\n2. Силиконовая жердочка - 1 шт;\n3. Выдвижной контейнер с двумя отсеками - 1 шт;\n4. Присоска - 4 шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except Exception as ex:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Прозрачная ванночка-купалка для купания шиншилл, грызунов с дверцей голубого цвета.
@dp.callback_query_handler(text='pets_2')
async def sale_pets_2(callback: types.CallbackQuery):
    try:
        if callback.data == 'pets_2':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/aJaGeDp')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-o/wc1000/6531007044.jpg'
            caption = f'<b>Прозрачная ванночка-купалка для купания шиншилл, грызунов с дверцей голубого цвета.</b>\n\nКупалка голубого цвета для мелких грызунов позволяет зверьку вычистить свою шерстку практически от любых видов загрязнений, играя роль песочной ванной, в которой питомец может вдоволь покувыркаться. Помимо непосредственно гигиенических процедур очищения, пребывание в песке доставляет грызуну много радости, поэтому регулярное предоставление животному ванночки с сыпучим наполнителем, благоприятно сказывается на настроении и самочувствии зверька.\n\n<b>Комплектация</b>\nВанночка - 1 шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except Exception as ex:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Тренировочная игрушка для дрессировки собак и кошек.
@dp.callback_query_handler(text='pets_3')
async def sale_pets_3(callback: types.CallbackQuery):
    try:
        if callback.data == 'pets_3':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/7X4J5lb')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-m/wc1000/6481288990.jpg'
            caption = f'<b>Тренировочная игрушка для дрессировки собак и кошек.</b>\n\nТренировочная игрушка для кормления и дрессировки домашних животных серого цвета идеально подходит для развлечения Ваших детей с любимыми питомцами. "Пистолет-катапульта" с автоматической подачей корма прост в использовании\n\n<b>Комплектация</b>\nИгрушка для подачи лакомства и дрессировки - 1 шт.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except Exception as ex:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Гриндер-когтерез для когтей бесшумный. Электрическая когтеточка для собак и кошек.
@dp.callback_query_handler(text='pets_4')
async def sale_pets_4(callback: types.CallbackQuery):
    try:
        if callback.data == 'pets_4':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/2GXLP9j')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-c/wc1000/6500998584.jpg'
            caption = f'<b>Гриндер-когтерез для когтей бесшумный. Электрическая когтеточка для собак и кошек.</b>\n\nГриндер для кошек и собак — это электрический когтерез, безопасный инструмент, не травмирующий когти животного. Также его можно назвать когтеточкой. Подходит для совместного использования с механической когтерезкой. Гриндером можно обтачивать острые углы когтей после стрижки. Он представляет собой устройство с насадкой-валиком, которая стачивает и шлифует коготь.\n\n<b>Комплектация</b>\n- Гриндер;\n- USB-провод.'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except Exception as ex:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# Вольер для собак, щенков, кошек, котят и других животных
@dp.callback_query_handler(text='pets_5')
async def sale_pets_5(callback: types.CallbackQuery):
    try:
        if callback.data == 'pets_5':
            ikb = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('КУПИТЬ НА OZON', url='https://ozon.ru/t/3eERnw3')
                ],
                [
                    InlineKeyboardButton('НАЗАД В МЕНЮ', callback_data='back')
                ]
            ])
            photo = 'https://ir.ozone.ru/s3/multimedia-0/wc1000/6508440960.jpg'
            caption = f'<b>Вольер для собак, щенков, кошек, котят и других животных.</b>\n\nВольер для собак, щенков, кошек, котят и других животных.\n\n<b>Комплектация</b>\n1. Вольер'
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=f'{caption}', reply_markup=ikb)
    except Exception as ex:
        logging.warning('Ошибка при обработки запроса')
    await callback.answer()


# === back menu
@dp.callback_query_handler(text='back')
async def aqua_back(callback: types.callback_query):
    await callback.message.answer(text='Наши зоотовары', reply_markup=sale_inline())
    await callback.answer()


@rate_limit(limit=3)
@dp.message_handler(IsGroup(), text=['/help'])
async def command_help(message: types.Message):
    link = hlink('🤖 наш бот', 'https://t.me/zoozavrbot')
    await message.answer(f"Нужна помощь? Напиши нашему боту {link}\n")


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text=['/help'])
async def command_help(message: types.Message):
    await message.answer(f"Выбери меню ниже, для помощи 👇", reply_markup=get_reply_keyboard())
