from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("سلام! من ربات توام. هر چی بگی، برات تکرار می‌کنم! 😄")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater("8139529574:AAGPOGoBKawJc42Z8m1qKf5EzhKQj80xp5Q", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
