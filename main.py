import asyncio

from telegram.add_chat import AddChat
from telegram.auto_auth import *


async def main():
    telegram_core = AutoAuth(os.path.join(os.path.dirname(__file__), 'auth', 'save_sessions'))

    # result_connect = await telegram_core.check_connect()
    #
    # if not result_connect:
    #     result_aut = await telegram_core.aut_start()
    #
    #     if not result_aut:
    #         print(f'Ошибка аккаунта')
    #         return False

    telegram_app = await telegram_core.start_tg()


    job_tg = AddChat(telegram_app)
    result_add = await job_tg.get_chat_members()
    # result_add = await job_tg.add_user_to_chat()

    print()


if __name__ == '__main__':
    asyncio.run(main())
