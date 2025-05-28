from db import check_user_exists, create_user
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def add_new_users(user_id):
    if not check_user_exists(user_id):
        create_user(user_id)


def get_menu_buttons():
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Случайная карта", callback_data="random_card_menu"),
            ],
            [
                InlineKeyboardButton("История матчей", callback_data="games_history_menu"),
            ],
            [
                InlineKeyboardButton("История компаний", callback_data="companies_history_menu"),
            ],
            [
                InlineKeyboardButton("Настроить дополнения", callback_data="expansions_settings_menu"),
            ],
        ]
    )
    return buttons
