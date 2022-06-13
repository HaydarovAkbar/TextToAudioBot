from battons import *
from database import Database
from gtts import gTTS
import docx2txt
from telegram import Update
from telegram.ext import CallbackContext
from telegram import ParseMode
import time

database_data = Database()


def add_database(update, context):
    try:
        chat_id = update.message.chat.id
        database_data.set(update.message.from_user.first_name, update.message.from_user.username, chat_id)
    except Exception as e:
        print(e)


def start(update, context):
    try:
        chat_id = update.message.chat.id
        if chat_id not in [i[3] for i in database_data.get_user()]:
            chat_id = update.message.chat.id
            database_data.set(update.message.from_user.first_name, update.message.from_user.username, chat_id)
        update.message.reply_html(text="🔥 <b>Assalomu alaykum, Textni ovozli ko'rinishda o'qib beradigan botga xush "
                                       "kelibsiz qaysi tildagi textni ovozli ko'rinishga o'tkarmoqchisiz tanlang\n\n"
                                       "🔥 Здравствуйте, и добро пожаловать в бота, который читает текст в аудио. "
                                       "Выберите язык, на котором вы хотите преобразовать текст в аудио.\n\n"
                                       "🔥 Hello, and welcome to the bot that reads the text in audio. "
                                       "Choose the language in which you want to convert the text to audio.</b>",
                                  reply_markup=lang_batton())
        return 1
    except Exception as e:
        print(e)


def add_lang(update, context):
    try:
        name = update.callback_query.message.chat.first_name
        query = update.callback_query
        chat_id = update.callback_query.message.chat.id
        database_data.update_user_lang(chat_id, query.data)

        # davlatini aniqlash

        lang = ""
        for key, value in all_lang.items():
            if value == query.data:
                lang = key

        all_lang_2 = til.get(query.data, None)

        if not all_lang_2:
            soz = til.get("boshqa")
            all_lang_2 = soz[0] + lang + soz[1]
        lan = query.data
        query.delete_message(timeout=15)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"<b>{name}!</b>😊\n" + "<i>" + all_lang_2 + "</i>",
                                 parse_mode="HTML",
                                 reply_markup=edit_batton(lan))
        return 1
    except Exception as e:
        print(e)


def comment(update, context):
    try:
        user_id = update.message.chat.id
        user = database_data.get_user_id(user_id)
        comment_user_text = comment_text.get(user[4],
                                             "You can send suggestions or references about the bot, we will definitely consider it")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="<b>" + comment_user_text + "</b>",
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
        return 2
    except Exception as e:
        print(e)


def send_comment(update: Update, context: CallbackContext):
    try:
        user = update.message

        user_id = update.message.chat.id
        user_ = database_data.get_user_id(user_id)
        msg_id = update.message.message_id  # (from_chat_id=758934089,message_id=msg_id,caption='reply xabar')
        context.bot.send_message(chat_id=758934089,
                                 text="Xabar: " + user.text + f"\n\n USER name: {user.chat.first_name}\nID:{user_id}\n@{user.chat.username}    tominidan yo'llandi")

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=send_comment_text.get(user_[4],
                                                            "Your message has been sent to the programmer😊 \nYou can click the Back button!"),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user_[4]))
    except Exception as e:
        print(e)


def back_(update, context):
    try:
        user = database_data.get_user_id(update.message.chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=back_text.get(user[4], "Let's continue !!!"),
                                 parse_mode="HTML",
                                 reply_markup=edit_batton(user[4]))
        return 1
    except Exception as e:
        print(e)


def about_bot(update, context):
    try:
        user_id = update.message.chat.id
        if user_id == 758934089:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="<b>Akbar Botga xush kelibsiz</b>!",
                                     parse_mode="HTML",
                                     reply_markup=admin_batton)
            return 3
        user = database_data.get_user_id(user_id)

        bot_about_text_ = bot_about_function(user[4])
        if not bot_about_text_:
            bot_about_text_ = bot_about_function('en')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=bot_about_text_,
                                 parse_mode=ParseMode.MARKDOWN_V2,
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        print(e)


def help_(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="♻️O'zbekcha textni ovozga aylantirish uchun sizga @ttsuzbot botni tavfsiya qilamiz!",
                             parse_mode="HTML", )


def speach(update: Update, context: CallbackContext):
    try:
        text = update.message.text
        user_id = update.message.chat.id
        user = database_data.get_user_id(user_id)
        a = update.message.reply_html(text=wait_text.get(user[4], wait_text.get('en')))
        if user[4] == 'uz':
            return help_(update, context)
        tts = gTTS(text=text, lang=user[4], slow="False")
        tts.save("Audio.mp3")
        context.bot.delete_message(
            timeout=1,
            chat_id=user_id,
            message_id=int(a.message_id))
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open("Audio.mp3", "rb"),
                               caption="@text_to_audiobot")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="<b>Please! Enter a word in the language you specify</b>",
                                 parse_mode="HTML", )


# Admin
def get_user(update, context):
    try:
        all_user = database_data.get_user_50()
        user_id = update.message.chat.id
        user = database_data.get_user_id(user_id)
        all_text = "{:<1} || {:<8} || {:<23}\n\n".format("Number", "Name", "Username")
        for item in all_user:
            try:
                all_text += "{:<1}). || <b>{:<8}</b> || @{:<23}\n".format(item[0], item[1], item[2])
            except:
                pass
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=all_text,
                                 # parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=str(e),
                                 )


# Reklama qismi !!!
def rek(update, context):
    user_id = update.message.chat.id
    user = database_data.get_user_id(user_id)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Reklama xabarini TEXT,VIDEO,RASM ko'rinishida yuborishingiz mumkin</b>!",
                             parse_mode="HTML",
                             reply_markup=back_batton(user[4]))
    return 4


def rek_video(update, context):
    text = update.message.caption
    video = update.message.video['file_id']
    user_id = update.message.chat.id
    user = database_data.get_user_id(user_id)
    if video:
        if user_id == 758934089:
            s = 0
            for item in database_data.get_data():
                try:
                    context.bot.send_video(chat_id=item[0],
                                           video=video,
                                           caption=text + "\n\n    @text_to_audiobot",
                                           disable_notification=True)
                    s += 1
                except Exception as e:
                    pass
            context.bot.send_message(chat_id=user_id,
                                     text=f"jo'natgan  xabaringiz {s}-ta userga bordi!",
                                     reply_markup=back_batton(user[4]))
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Siz Video jo'natishingiz kerak edi adashdingiz",
                                 reply_markup=back_batton(user[4]))


def rek_photo(update, context):
    user_id = update.message.chat.id
    user = database_data.get_user_id(user_id)
    caption = update.message.caption
    photo = update.message.photo[0]["file_id"]
    if photo:
        if user_id == 758934089:
            s = 0
            for item in database_data.get_data():
                try:
                    context.bot.send_photo(chat_id=item[0],
                                           photo=photo,
                                           caption=caption + "\n\n    @text_to_audiobot",
                                           disable_notification=True)
                    s += 1
                except Exception as e:
                    pass
            context.bot.send_message(chat_id=user_id,
                                     text=f"jo'natgan  xabaringiz {s}-ta userga bordi!",
                                     reply_markup=back_batton(user[4]))
        else:
            context.bot.send_message(chat_id=user_id,
                                     text=f"Uzr sizni tanimadim🧐",
                                     reply_markup=back_batton(user[4]))
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Siz Rasm jo'natishingiz kerak edi adashdingiz!",
                                 reply_markup=back_batton(user[4]))


def rek_text(update, context):
    user_id = update.message.chat.id
    user = database_data.get_user_id(user_id)
    text = update.message.text
    if user_id == 758934089:
        s = 0
        for item in database_data.get_data():
            try:
                context.bot.send_message(chat_id=item[0], text=text + "\n\n    @text_to_audiobot")
                s += 1
            except Exception as e:
                pass
        context.bot.send_message(chat_id=user_id,
                                 text=f"Jo'natgan  xabaringiz {s}-ta userga bordi!",
                                 reply_markup=back_batton(user[4]))
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Uzr sizni tanimadim🧐",
                                 reply_markup=back_batton(user[4]))


def admin_(update, context):
    try:
        user_id = update.message.chat.id
        user = database_data.get_user_id(user_id)
        context.bot.send_message(chat_id=user_id,
                                 text=f"Id sini kiriting va textni kiriting (123145122,Text ko'rinishida)",
                                 reply_markup=back_batton(user[4]))
        return 5
    except Exception as e:
        print(e)


def send_admin_to_user(update, context):
    try:
        user_id = update.message.chat.id
        user = database_data.get_user_id(user_id)
        text = update.message.text
        index_ = text.index(",")
        id = text[:index_]
        text_ = text[index_ + 1:]
        context.bot.send_message(chat_id=id,
                                 text=text_,
                                 reply_markup=back_batton(user[4]))
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Xabar yuborildi!", )
        return 1
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Xabar yuborilmadi!", )


# import PyPDF2

# def doc(update :Update,context:CallbackContext):
#     try:
#         user_id = update.message.chat.id
#         user = database_data.get_user_id(user_id)
#         a = update.message.reply_html(text=wait_text.get(user[4],wait_text.get('en')))
#         name = update.message.document.file_name
#         file = update.message.document.get_file(timeout=0.5)
#         aa = file.download('document.pdf')
#         print(type(a))
#         if '.pdf' in name:
#             pdf_file = open("document.pdf",'r')
#             print(pdf_file.read())
#             pdf_read = PyPDF2.PdfFileReader(pdf_file)
#             pdf_f = pdf_read.getPage(0)
#             text = pdf_f.extractText()
#             print(text)
#         text = docx2txt.process("document")
#         if user[4] == 'uz':
#             return help_(update,context)
#         tts = gTTS(text=text, lang=user[4],slow="False")
#         tts.save("Audio.mp3")
#         context.bot.delete_message(
#             timeout=1,
#             chat_id=user_id,
#             message_id=int(a.message_id))
#         context.bot.send_audio(chat_id=user_id,
#                                audio=open("Audio.mp3","rb"),
#                                caption=f"{name}  🔄  Audio.mp3 ✅\n\n@text_to_audiobot")
#     except Exception as e:
#         print(e)
#     return 1

def doc(update: Update, context: CallbackContext):
    try:
        user_id = update.message.chat.id
        user = database_data.get_user_id(user_id)
        a = update.message.reply_html(text=wait_text.get(user[4], wait_text.get('en')))
        name = update.message.document.file_name
        file = update.message.document.get_file(timeout=0.5)
        file.download('document')
        text = docx2txt.process("document")
        if user[4] == 'uz':
            return help_(update, context)
        tts = gTTS(text=text, lang=user[4], slow="False")
        tts.save("Audio.mp3")
        time.sleep(10)
        context.bot.delete_message(
            timeout=1,
            chat_id=user_id,
            message_id=int(a.message_id))
        context.bot.send_audio(chat_id=user_id,
                               audio=open("Audio.mp3", "rb"),
                               caption=f"{name}  🔄  Audio.mp3 ✅\n\n@text_to_audiobot")
    except Exception as e:
        print(e)
    return 1
