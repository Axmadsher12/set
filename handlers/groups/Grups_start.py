from aiogram import types
from loader import dp
from filters.Grups import Grups
@dp.message_handler(Grups(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text="Grups dan start bosildi")
