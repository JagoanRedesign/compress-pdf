from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Support', url='t.me/Chat4Robot'),
            InlineKeyboardButton('Channel', url='t.me/DutabotID')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/Chat4Robot'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
