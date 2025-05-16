import os
from typing import Any, Callable, Coroutine, Dict, Optional

from dotenv import load_dotenv
from logger import LOGGER, logger_init
from telegram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from utils import update_message

load_dotenv()


async def wake_up(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat = update.effective_chat
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
                InlineKeyboardButton("Настроить дополнения", callback_data="additional_settings_menu"),
            ],
        ]
    )
    LOGGER.info(f"Пользователь {chat.username} вошел в бота")
    await context.bot.send_message(chat_id=chat.id, text="Спасибо, что включили меня", reply_markup=buttons)


async def error(query: CallbackQuery) -> None:
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
                InlineKeyboardButton("Настроить дополнения", callback_data="additional_settings_menu"),
            ],
        ]
    )
    LOGGER.info(f"У пользователя {query.from_user.username} произошла ошибка, query: {query.data}")
    LOGGER.debug(f"query: {query.data}")
    LOGGER.debug(f"buttons: {buttons}")
    await update_message(query, buttons, "Что-то пошло не так, начнём с начала?")


async def buttons_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    FUNCTIONS: Dict[str, Callable[[CallbackQuery, Optional[str]], Coroutine[Any, Any, None]]] = {
        "random_card_menu": ...,
    }
    chat = update.effective_chat
    await context.bot.send_chat_action(chat_id=chat.id, action="typing")
    query = update.callback_query
    await query.answer()
    LOGGER.info(f"Пользователь {query.from_user.username} нажал кнопку {query.data}")
    if query.data in FUNCTIONS.keys():
        await FUNCTIONS[query.data](query)  # type: ignore
    else:
        await error(query)


def main() -> None:
    logger_init()
    LOGGER.info("Бот запущен")
    auth_token = os.getenv("TOKEN")
    application = Application.builder().token(auth_token).read_timeout(30).connect_timeout(30).build()
    application.add_handler(CallbackQueryHandler(buttons_handler))
    application.add_handler(CommandHandler("start", wake_up))
    application.run_polling(allowed_updates=Update.ALL_TYPES, timeout=30)


if __name__ == "__main__":
    main()