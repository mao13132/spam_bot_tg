from pyrogram import Client
from auth.settings import api_id, api_hash

import os

class AutoAuth:
    def __init__(self, path):
        self.path = path + f'\\{api_id}'

    async def aut_start(self):
        app = Client(self.path, api_id, api_hash)

        app.run()


    async def check_connect(self):
        app = Client(self.path, api_id, api_hash)

        return app.connect()

    async def start_tg(self):
        app = Client(self.path, api_id, api_hash)

        await app.start()

        return app





