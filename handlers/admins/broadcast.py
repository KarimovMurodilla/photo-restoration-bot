import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import exceptions, executor

from loader import dp, db, bot

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')


async def get_users():
    """
    Возвращает список пользователей
    """
    users = await db.get_all_users()
    return users


async def send_message(user_id: int, text: str, disable_notification: bool = False) -> bool:
    """
    Безопасный отправитель сообщений

    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcaster(text) -> int:
    """
    Простая рассылка

    :return: Количество отправленных сообщений
    """
    count = 0
    try:
        for user in await get_users():
            if await send_message(user.user_id, text):
                count += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        log.info(f"{count} сообщений отправлено успешно.")

    return count