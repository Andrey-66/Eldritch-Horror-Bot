from typing import Dict, List

from logger import LOGGER
from telegram import CallbackQuery, InlineKeyboardMarkup


async def update_message(
    query: CallbackQuery, buttons: InlineKeyboardMarkup, text: str, parse_mode=None, media=None
) -> None:
    if not query.message.text or media:
        await query.delete_message()
        if media:
            await query.get_bot().send_photo(
                chat_id=query.message.chat.id, photo=media, caption=text, reply_markup=buttons, parse_mode=parse_mode
            )
        else:
            await query.get_bot().send_message(
                chat_id=query.message.chat.id, text=text, reply_markup=buttons, parse_mode=parse_mode
            )
    else:
        LOGGER.debug(f"Пользователь {query.from_user.username} обновил сообщение")
        LOGGER.debug(f"query: {query.data}")
        LOGGER.debug(f"buttons: {buttons}")
        LOGGER.debug(f"text: {text}")
        LOGGER.debug(f"parse_mode: {parse_mode}")
        await update_message_text(query, buttons, text, parse_mode)


async def update_message_text(query: CallbackQuery, buttons: InlineKeyboardMarkup, text: str, parse_mode=None) -> None:
    if query.message.reply_markup == buttons and query.message.text == text:
        return
    await query.edit_message_text(text=text, reply_markup=buttons, parse_mode=parse_mode)