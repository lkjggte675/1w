Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import logging
... import time
... from telegram.ext import Application
... from bot_handlers import register_handlers
... 
... def setup_bot():
...     """Настройка основного приложения бота"""
...     logging.basicConfig(
...         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
...         level=logging.INFO
...     )
...     app = Application.builder().token("ВАШ_ТОКЕН_БОТА").build()
...     register_handlers(app)
...     return app
... 
... def run_bot():
...     """Запуск бота с обработкой ошибок"""
...     while True:
...         try:
...             app = setup_bot()
...             logging.info("✅ Бот успешно запущен")
...             app.run_polling()
...         except Exception as e:
...             logging.error(f"🚨 Ошибка: {e}. Перезапуск через 10 секунд...")
...             time.sleep(10)
... 
... if name == "main":
