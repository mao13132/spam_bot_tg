import os

from pyrogram import Client

from json import dump, loads

from auth.settings import id_chat



class AddChat:
    def __init__(self, app: Client):
        self.app = app

    async def add_user_to_chat(self):

        result = await self.app.add_chat_members(id_chat, '@JrMcKinner')

        print(result)

    async def _create_path(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            dump('', file)

    def save_json(self, member):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            dump(loads(str(member)), file, indent=4, ensure_ascii=False)

    async def get_chat_members(self):
        self.file_name = 'pars_members\\' + str(id_chat)[1:] + '.json'


        count = 0
        async for member in self.app.get_chat_members(id_chat):
            self.save_json(member)
            count += 1


        print(f'Всего участников: {count}')

