from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
hp_Buttons=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CORE i3π₯"),
            KeyboardButton(text='CORE i5π₯'),
        ],
        [
            KeyboardButton(text='CORE i7π₯'),
            KeyboardButton(text='CORE i9π₯'),
        ],
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text='Ortgaπ')
        ]
    ],
            resize_keyboard=True
)