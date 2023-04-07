from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from data import config
from utils.db_api.db_gino import db

# #Настройки логирования
# now = datetime.datetime.now()
# file_log = logging.FileHandler('./logs/{}-{}.log'.format(now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")))
# console_out = logging.StreamHandler()
# logging.basicConfig(handlers=(file_log, console_out), format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG)


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

__all__ = ['bot', 'storage', 'dp', 'db']