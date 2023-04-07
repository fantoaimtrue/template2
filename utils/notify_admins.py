import logging
from loader import bot
from aiogram import Dispatcher

from data.config import admins

#
#
async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            # text = 'Бот запущен!'
            # await dp.bot.send_message(chat_id=admin, text=text)
            pass
        except Exception as err:
            logging.exception(err)


### Остановка бота
async def on_shutdown(dp):
    logging.warning('Shutting down..')

    logging.warning('Bye!')