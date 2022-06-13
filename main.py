from telegram.ext import Updater, CallbackQueryHandler, Filters, CommandHandler, ConversationHandler, MessageHandler
import timeit
from methods import *
from Battons import *

updater = Updater(Token, use_context=True, workers=1000)
dispatcher = updater.dispatcher

commands = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        CallbackQueryHandler(add_lang),

        MessageHandler(Filters.regex('^(' + 'Сменить язык' + ')$'), start),
        MessageHandler(Filters.regex('^(' + "Tilni o'zgartirish" + ')$'), start),
        MessageHandler(Filters.regex('^(' + 'Change language' + ')$'), start),

        MessageHandler(Filters.regex('^(' + 'Fikr bildirish' + ')$'), comment),
        MessageHandler(Filters.regex('^(' + "Комментарий" + ')$'), comment),
        MessageHandler(Filters.regex('^(' + 'Comment' + ')$'), comment),

        MessageHandler(Filters.regex('^(' + 'назад' + ')$'), back_),
        MessageHandler(Filters.regex('^(' + "orqaga" + ')$'), back_),
        MessageHandler(Filters.regex('^(' + 'back' + ')$'), back_),

        MessageHandler(Filters.regex('^(' + 'Bot haqida' + ')$'), about_bot),
        MessageHandler(Filters.regex('^(' + "О боте" + ')$'), about_bot),
        MessageHandler(Filters.regex('^(' + 'About bot' + ')$'), about_bot),
    ],
    states={
        1: [CommandHandler('start', start),
            CallbackQueryHandler(add_lang),

            MessageHandler(Filters.regex('^(' + 'Сменить язык' + ')$'), start),
            MessageHandler(Filters.regex('^(' + "Tilni o'zgartirish" + ')$'), start),
            MessageHandler(Filters.regex('^(' + 'Change language' + ')$'), start),

            MessageHandler(Filters.regex('^(' + 'Fikr bildirish' + ')$'), comment),
            MessageHandler(Filters.regex('^(' + "Комментарий" + ')$'), comment),
            MessageHandler(Filters.regex('^(' + 'Comment' + ')$'), comment),

            MessageHandler(Filters.regex('^(' + 'назад' + ')$'), back_),
            MessageHandler(Filters.regex('^(' + "orqaga" + ')$'), back_),
            MessageHandler(Filters.regex('^(' + 'back' + ')$'), back_),

            MessageHandler(Filters.regex('^(' + 'Bot haqida' + ')$'), about_bot),
            MessageHandler(Filters.regex('^(' + "О боте" + ')$'), about_bot),
            MessageHandler(Filters.regex('^(' + 'About bot' + ')$'), about_bot),
            ],
        2: [
            CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + 'назад' + ')$'), back_),
            MessageHandler(Filters.regex('^(' + "orqaga" + ')$'), back_),
            MessageHandler(Filters.regex('^(' + 'back' + ')$'), back_),
            MessageHandler(Filters.text, send_comment),
        ],
        3: [
            CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + 'назад' + ')$'), back_),
            MessageHandler(Filters.regex('^(' + "orqaga" + ')$'), back_),
            MessageHandler(Filters.regex('^(' + 'back' + ')$'), back_),

            MessageHandler(Filters.regex('^(' + '🤖 Bot Foydalanuvchilari 🤖' + ')$'), get_user),
            MessageHandler(Filters.regex('^(' + "❇️ Reklama 🌉" + ')$'), rek),
            MessageHandler(Filters.regex('^(' + "👨🏻‍💻 Userga javob 👨🏻‍💻" + ')$'), admin_),
        ],
        4: [
            CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + 'назад' + ')$'), back_),
            MessageHandler(Filters.regex('^(' + "orqaga" + ')$'), back_),
            MessageHandler(Filters.regex('^(' + 'back' + ')$'), back_),

            MessageHandler(Filters.text, rek_text),
            MessageHandler(Filters.photo, rek_photo),
            MessageHandler(Filters.video, rek_video),
        ],
        5: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + 'назад' + ')$'), back_),
            MessageHandler(Filters.regex('^(' + "orqaga" + ')$'), back_),
            MessageHandler(Filters.regex('^(' + 'back' + ')$'), back_),
            MessageHandler(Filters.text, send_admin_to_user), ]
    },
    fallbacks=[MessageHandler(Filters.text, speach),
               MessageHandler(Filters.document, doc),
               ],
    run_async=True
)

dispatcher.add_handler(commands)
updater.start_polling()
print("Start Polling")
