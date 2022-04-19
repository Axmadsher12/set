from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
Kompyuterlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Acer🖥"),
            KeyboardButton(text="Asus🖥")
        ],
        [
            KeyboardButton(text='Dell🖥'),
            KeyboardButton(text='hp🖥')
        ],
        [
            KeyboardButton(text='Lenovo🖥')
        ]
    ],
            resize_keyboard=True
)