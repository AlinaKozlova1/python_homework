from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5739889419:AAEUjpFoE0F4zkJYKI2pUd_htvxe_kFkdQk").build()

app.add_handler(CommandHandler("hello", hello))

print("server starts")

app.run_polling()
