from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler

app = Flask(__name__)

TOKEN = '6561748036:AAEGF_LM_8_kYojtfCnj3gpJ11pA0_Qu35Q'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello from Koyeb!')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
