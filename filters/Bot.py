from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class Bot(BoundFilter):
    async def Bot_check(self,message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE