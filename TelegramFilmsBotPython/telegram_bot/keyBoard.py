from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


keyBoard_Start = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "/info"),
            KeyboardButton(text = "/catalog")
        ]
    ],
    resize_keyboard = True
)


keyBoard_Info = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "/catalog")
        ]
    ],
    resize_keyboard = True
)


keyBoard_Catalog = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "/kion"),
            KeyboardButton(text = "/ivi"),
            KeyboardButton(text = "/premier")
        ],
        [
            KeyboardButton(text = "/info")
        ]
    ],
    resize_keyboard = True
)


keyBoard_Kion = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "/popular_now_kion"),
            KeyboardButton(text = "/new_kion"),
            KeyboardButton(text = "/fantastic_kion")
        ],
        [
            KeyboardButton(text = "/comedy_kion"),
            KeyboardButton(text = "/action_kion")
        ],
        [
            KeyboardButton(text = "/catalog")
        ]
    ],
    resize_keyboard = True
)


keyBoard_Ivi = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "/best_ivi"),
            KeyboardButton(text = "/comedy_ivi"),
            KeyboardButton(text = "/fantastic_ivi")
        ],
        [
            KeyboardButton(text = "/adventures_ivi"),
            KeyboardButton(text = "/action_ivi")
        ],
        [
            KeyboardButton(text = "/catalog")
        ]
    ],
    resize_keyboard = True
)


keyBoard_Premier = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "/drama_premier"),
            KeyboardButton(text = "/adventures_premier"),
            KeyboardButton(text = "/fantastic_premier")
        ],
        [
            KeyboardButton(text = "/comedy_premier"),
            KeyboardButton(text = "/detektiv_premier")
        ],
        [
            KeyboardButton(text = "/catalog")
        ]
    ],
    resize_keyboard = True
)