from aiogram import types
from keyboards.default.Acer.Acer_button import Acer_Buttons
from keyboards.default.Asus.Asus_button import Asus_Buttons
from keyboards.default.Dell.Dell_button import Dell_Buttons
from keyboards.default.Lenovo.Lenovo_button import Lenovo_Buttons
from keyboards.default.hp.hp_button import hp_Buttons
from keyboards.default.Kompyuterlar import Kompyuterlar
from loader import dp


@dp.message_handler(text='Acer🖥')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=Acer_Buttons)


@dp.message_handler(text='Dell🖥')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=Dell_Buttons)


@dp.message_handler(text='Asus🖥')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=Asus_Buttons)


@dp.message_handler(text='hp🖥')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=hp_Buttons)


@dp.message_handler(text='Lenovo🖥')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=Lenovo_Buttons)


@dp.message_handler(text='Menu')
async def bot_echo(message: types.Message):
    await message.answer(text='CORE i ni tanlang!', reply_markup=Kompyuterlar)



