from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
Lenovo_Buttons=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CORE i3🖥"),
            KeyboardButton(text='CORE i5🖥'),
        ],
        [
            KeyboardButton(text='CORE i7🖥'),
            KeyboardButton(text='CORE i9🖥'),
        ],
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text='Ortga🔙')
        ]
    ],
            resize_keyboard=True
)