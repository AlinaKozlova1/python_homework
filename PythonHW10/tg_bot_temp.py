from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5431996543:AAE9XcLsh9lctRDZoWiYiboCzUe1ns0NcAw").build()

app.add_handler(CommandHandler("hello", hello))

print("server starts")

app.run_polling()
