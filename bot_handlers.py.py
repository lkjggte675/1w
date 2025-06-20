Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler

# Конфигурация
REGISTER_URL = "https://1wzyuh.com/casino/list?open=register&p=un32"
PROMO_CODE = "WINNERR9"
CHANNEL_ID = "https://t.me/+8vpuxbWrVTw3MzBi"

def main_menu():
    """Главное меню бота"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Игры", callback_data="games_menu")],
        [InlineKeyboardButton("📚 Инструкция", callback_data="instructions")],
        [InlineKeyboardButton("🚀 Регистрация", url=REGISTER_URL)]
    ])

async def start(update: Update, context: CallbackContext):
    """Обработчик команды /start"""
    await update.message.reply_text(
        f"🎮 Добро пожаловать!\n\n"
        f"🔹 Промокод: <code>{PROMO_CODE}</code>\n"
        f"🔹 Канал: {CHANNEL_ID}\n\n"
        "👇 Выберите действие:",
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

async def button_handler(update: Update, context: CallbackContext):
    """Обработчик всех callback кнопок"""
    query = update.callback_query
...     await query.answer()
...     
...     if query.data == "games_menu":
...         await show_games_menu(query)
...     elif query.data == "instructions":
...         await show_instructions(query)
... 
... async def show_games_menu(query):
...     """Меню выбора игр"""
...     games_menu = InlineKeyboardMarkup([
...         [InlineKeyboardButton("🪙 CoinFlip", callback_data="game_coinflip")],
...         [InlineKeyboardButton("✈️ Lucky Jet", callback_data="game_luckyjet")],
...         [InlineKeyboardButton("💣 Mines", callback_data="game_mines")],
...         [InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")]
...     ])
...     await query.edit_message_text(
...         text="🎮 Выберите игру:",
...         reply_markup=games_menu
...     )
... 
... async def show_instructions(query):
...     """Отображение инструкции"""
...     await query.edit_message_text(
...         text=f"📚 <b>Инструкция</b>\n\n"
...              "1. Нажмите <b>🚀 Регистрация</b>\n"
...              f"2. Введите промокод: <code>{PROMO_CODE}</code>\n"
...              "3. Пополните баланс от 500₽\n"
...              "4. Получите <b>+150%</b> к депозиту\n\n"
...              f"💬 Поддержка: @ваш_поддержка",
...         reply_markup=InlineKeyboardMarkup([
...             [InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")],
...             [InlineKeyboardButton("✨ Зарегистрироваться", url=REGISTER_URL)]
...         ]),
...         parse_mode="HTML"
...     )
... 
... def register_handlers(app):
...     """Регистрация всех обработчиков"""
...     app.add_handler(CommandHandler("start", start))
