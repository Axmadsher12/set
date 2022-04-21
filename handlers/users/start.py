from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.Kompyuterlar import Kompyuterlar
from filters.Bot import Bot
from loader import dp,baza,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    Name = message.from_user.first_name
    Username = message.from_user.username
    Telegram_id = message.from_user.id
    try:
        baza.add_User_Kompyuterlar_123bot(Name=Name,Username=Username,Telegram_id=Telegram_id)
    except Exception as z:
        await message.answer(f"Salom, {z}!")

    await message.answer(text=f'Kompyuter turini tnlang',reply_markup=Kompyuterlar)

@dp.message_handler(commands='Reklama')
async def bot_start(message: types.Message):
    await message.answer(text='Reklama')


' Message_users '
#@dp.message_handler(commands='Reklama',chat_id='')
#async def bot_start(message: types.Message):
#    sellect_all_users=baza.sellect_all_users_Kompyuterlar_123bot()
#    for Users in sellect_all_users:
#        await bot.send_message(chat_id=Users[1],text='@Kompyuterlar_123bot')
