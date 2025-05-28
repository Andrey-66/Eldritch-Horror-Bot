from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from constants import (NAME_CITIES_IN_RUIN, NAME_FORSAKEN_LORE,
                       NAME_MASKS_OF_NYARLATHOTEP, NAME_MOUNTAINS_OF_MADNESS,
                       NAME_SIGNS_OF_CARCOSA, NAME_STRANGE_REMNANTS,
                       NAME_THE_DREAMLANDS, NAME_UNDER_THE_PYRAMIDS)
from db import check_expansion
from logger import LOGGER


def create_expansions_buttons(user_id):
    LOGGER.info(f"Создание кнопок для пользователя {user_id}")
    buttons = []
    param = "OFF"
    if check_expansion(user_id, "forsaken_lore"):
        param = "ON"
    buttons.append([InlineKeyboardButton(f"[{param}]: {NAME_FORSAKEN_LORE}", callback_data="expansion_forsaken_lore")])
    param = "OFF"
    if check_expansion(user_id, "mountains_of_madness"):
        param = "ON"
    buttons.append(
        [
            InlineKeyboardButton(
                f"[{param}]: {NAME_MOUNTAINS_OF_MADNESS}", callback_data="expansion_mountains_of_madness"
            )
        ]
    )
    param = "OFF"
    if check_expansion(user_id, "strange_remnants"):
        param = "ON"
    buttons.append(
        [InlineKeyboardButton(f"[{param}]: {NAME_STRANGE_REMNANTS}", callback_data="expansion_strange_remnants")]
    )
    param = "OFF"
    if check_expansion(user_id, "under_the_pyramids"):
        param = "ON"
    buttons.append(
        [InlineKeyboardButton(f"[{param}]: {NAME_UNDER_THE_PYRAMIDS}", callback_data="expansion_under_the_pyramids")]
    )
    param = "OFF"
    if check_expansion(user_id, "signs_of_carcosa"):
        param = "ON"
    buttons.append(
        [InlineKeyboardButton(f"[{param}]: {NAME_SIGNS_OF_CARCOSA}", callback_data="expansion_signs_of_carcosa")]
    )
    param = "OFF"
    if check_expansion(user_id, "the_dreamlands"):
        param = "ON"
    buttons.append(
        [InlineKeyboardButton(f"[{param}]: {NAME_THE_DREAMLANDS}", callback_data="expansion_the_dreamlands")]
    )
    param = "OFF"
    if check_expansion(user_id, "cities_in_ruin"):
        param = "ON"
    buttons.append(
        [InlineKeyboardButton(f"[{param}]: {NAME_CITIES_IN_RUIN}", callback_data="expansion_cities_in_ruin")]
    )
    param = "OFF"
    if check_expansion(user_id, "masks_of_nyarlathotep"):
        param = "ON"
    buttons.append(
        [
            InlineKeyboardButton(
                f"[{param}]: {NAME_MASKS_OF_NYARLATHOTEP}", callback_data="expansion_masks_of_nyarlathotep"
            )
        ]
    )
    buttons.append([InlineKeyboardButton("Назад", callback_data="menu")])
    return InlineKeyboardMarkup(buttons)
