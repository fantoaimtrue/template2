import datetime
from asyncpg import UniqueViolationError
from utils.db_api.schemas.chat_user import ChatUser


# Добавляем пользователя из чата в БД
async def add_chat_user(user_id: int, first_name: str, last_name: str, reputation: int,
                        total_help: int, mutes: int, last_rep_boost, last_help_boost):
    try:
        chat_user = ChatUser(user_id=user_id, first_name=first_name, last_name=last_name, reputation=reputation,
                             total_help=total_help,
                             mutes=mutes, last_rep_boost=last_rep_boost, last_help_boost=last_help_boost)
        await chat_user.create()
    except UniqueViolationError:
        print('Регистрация не создана')


# Проверяем есть ли юзер написавший нам сообщение в БД
async def check_chat_user(message):
    if message.reply_to_message:
        # Если не удалось получить юзера из БД
        if await select_chat_user(message.reply_to_message.from_user.id) is None:
            # Пытается его добавить
            await add_chat_user(
                user_id=message.reply_to_message.from_user.id,
                first_name=message.reply_to_message.from_user.first_name,
                last_name=message.reply_to_message.from_user.last_name,
                reputation=0,
                total_help=0,
                mutes=0,
                last_rep_boost=datetime.datetime.now() - datetime.timedelta(hours=4),
                last_help_boost=datetime.datetime.now() - datetime.timedelta(hours=4)
            )
        else:
            pass
    else:
        # Если не удалось получить юзера из БД
        if await select_chat_user(message.from_user.id) is None:
            # Пытаемся его добавить
            await add_chat_user(
                user_id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                reputation=0,
                total_help=0,
                mutes=0,
                last_rep_boost=datetime.datetime.now() - datetime.timedelta(hours=4),
                last_help_boost=datetime.datetime.now() - datetime.timedelta(hours=4)
            )


async def select_chat_user(user_id: int):
    chat_user = await ChatUser.query.where(ChatUser.user_id == user_id).gino.first()
    return chat_user
