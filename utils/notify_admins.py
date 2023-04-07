import logging
from loader import bot
from aiogram import Dispatcher

from data.config import admins
# from pyngrok import ngrok
# from data.config import NGROK_TOKEN

# подключение к серверу NGROK
# ngrok.set_auth_token(NGROK_TOKEN)
# http_tunnel = ngrok.connect(5000, bind_tls=True)
#
# # webhook settings
#
# WEBHOOK_HOST = http_tunnel.public_url
# WEBHOOK_PATH = ''
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# # webserver settings
# WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_PORT = 5000
#
#
# async def on_startup_notify(dp: Dispatcher):
#     await bot.set_webhook(WEBHOOK_URL)
#     for admin in admins:
#         try:
#             # text = 'Бот запущен!'
#             # await dp.bot.send_message(chat_id=admin, text=text)
#             pass
#         except Exception as err:
#             logging.exception(err)


### Остановка бота
async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # Remove webhook (not acceptable in some cases)
    # await bot.delete_webhook()

    # ngrok.disconnect(http_tunnel.public_url)

    logging.warning('Bye!')