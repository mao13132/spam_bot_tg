from pyrogram import Client
from auth.settings import api_id, api_hash

import os

class AutoAuth:
    def __init__(self, path):
        self.path = path + f'\\{api_id}.session'

    def aut_start(self):
        app = Client(self.path, api_id, api_hash)
        print()


