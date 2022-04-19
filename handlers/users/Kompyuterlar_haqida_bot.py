from aiogram import types
from keyboards.default.Acer.Acer_button import Acer_Buttons
from loader import dp,bot


@dp.message_handler(text='Acer🖥')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=Acer_Buttons)