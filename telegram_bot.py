from telegram.ext import Application, CommandHandler

API_KEY = "7492917306:AAENIJ7t91HFpT328eHAO-ZdmMQrCUHuM34"

async def start(update, context):
    name = update.effective_user.first_name
    message = f"Hello,{name} Welcome to my bot"
    await update.message.reply_text(message)

async def help(update, context):
    await update.message.reply_text("this is a help message")


application = Application.builder().token(API_KEY).build()

application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))

application.run_polling()