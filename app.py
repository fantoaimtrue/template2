from aiogram.utils.executor import start_polling
from utils.notify_admins import on_shutdown


async def on_startup(dp):
    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Подключение к PostgreSQL')
    await on_startup(dp)

    print('Удаление БД')
    await db.gino.drop_all()

    print('Создание таблиц')
    await db.gino.create_all()

    print('Готово')

    # from utils.notify_admins import on_startup_notify
    # await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Bot was started')


if __name__ == "__main__":
    from handlers import dp

    # На пулинге
    start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True
    )
