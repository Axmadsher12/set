from aiogram import types
from loader import dp
from filters.Kanal import Kanal
@dp.message_handler(Kanal(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text="Kanaldan start bosildi")
