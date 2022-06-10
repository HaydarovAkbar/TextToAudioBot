from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from database import Database


dbs = Database()

sonlar = {
    '0' : "0️⃣",
    '1' : "1️⃣",
    '2' : "2️⃣",
    '3' : "3️⃣",
    '4' : "4️⃣",
    '5' : "5️⃣",
    '6' : "6️⃣",
    '7' : "7️⃣",
    '8' : "8️⃣",
    '9' : "9️⃣",
}

# Bot TOKEN
Token = "1466245327:AAHK4PblP-YiiARa1Qpa439AUQGe5IBZ0B4"

_langs = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese"
}

all_lang = {
    "England": "en",
    "Russian": "ru",
    "Spanish": "es",
    "Portugal": "pt",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Gujarati":"gu",
    "Tamil":"ta",
    "Indonesia": "id",
    "Italy": 'it',
    "Japanese": "ja",
    "Korean": "ko",
    "Norwegian":"nb",
    "Turkish": 'tr',
    "China": "zh-CN",
    "Arabic":"ar",
    "Kannada":"kn",
    "Malaysia":"ms",
    "Chinese":"zh-CN",
}
# "Uzbekistan": "uz",

admin_batton = ReplyKeyboardMarkup([
    ["🤖 Bot Foydalanuvchilari 🤖","👨🏻‍💻 Userga javob 👨🏻‍💻"],
    ["❇️ Reklama 🌉","orqaga"],
],resize_keyboard=True)

til = {
    "uz": "siz o'zbek tilini tanladingiz endi siz o'zbek tilida so'z kiritishingiz mumkin",
    "ru": "вы выбрали русском языке, теперь вы можете вводить слова на русском языке",
    "en": "you have chosen English, now you can enter a word in English",
    "boshqa":["You have selected ",", you can enter words in the language you specify"]
}

comment_text = {
    "uz":"Bot haqida takliflar yoki murojaatlarni yuborishingiz mumkin, Biz uni albatta ko'rib chiqamiz",
    "ru":"Вы можете присылать предложения или отзывы о боте, мы обязательно рассмотрим",
}
send_comment_text = {
    "uz":"Xabaringiz dasturchiga yubirildi😊\nOrqaga qaytish tugmasini bosishingiz mumkin!",
    "ru":"Ваше сообщение отправлено программисту😊 \nВы можете нажать кнопку Назад!",
}
back = {
    "uz":"orqaga",
    "ru":"назад"
}

back_text = {
    "uz":"Davom etamiz!!!",
    "ru":"Давай продолжим !!!"
}

batton_ = {
    "uz": ["Tilni o'zgartirish", "Fikr bildirish", "Bot haqida"],
    'ru': ["Сменить язык", "Комментарий", "О боте"],
    'en': ["Change language", "Comment", "About bot"]
}
def bot_about_function(lang='en'):
    users_count_ = str(len(dbs.get_data()))
    user_count = ""

    for i in users_count_:
        user_count += sonlar.get(i)
    bot_about_text = {
        "uz":f"🤖 Text To Audio Bot\n\n🔹 Foydalanuvchilar soni: {user_count}\n 🔹Ishga tushirilgan vaqti: 25/05/2021\n🔹 Dasturchi: [Akbar](tg://user?id=758934089)",
        "ru":f"🤖  Text To Audio Bot\n\n🔹 Количество пользователей: {user_count} \n🔹 Дата начала: 25/05/2021 \n🔹 Разработчик: [Akbar](tg://user?id=758934089)",
        "en":f"🤖  Text To Audio Bot\n\n🔹 Number of Users: {user_count} \n🔹 Start Time: 25/05/2021 \n🔹 Developer: [Akbar](tg://user?id=758934089)"
    }
    return bot_about_text.get(lang)

def lang_batton():
    result, res = [], []
    for key, value in all_lang.items():
        if len(res) == 2:
            result.append(res)
            res = [InlineKeyboardButton(key, callback_data=value)]
        else:
            res.append(InlineKeyboardButton(key, callback_data=value))
    result.append(res)
    batton = InlineKeyboardMarkup(result)
    return batton


def edit_batton(lang):
    dataa = batton_.get(lang, ["Change language", "Comment", "About bot"])
    batton = ReplyKeyboardMarkup([
        [dataa[0], dataa[1]],
        [dataa[2]]
    ], resize_keyboard=True)
    return batton
def back_batton(lang):
    dataa = back.get(lang,"back")
    batton = ReplyKeyboardMarkup([
        [dataa],
    ], resize_keyboard=True)
    return batton

wait_text = {
    "uz":"<code>Bu biroz vaqt olishi mumkin iltimos kuting...🖐</code>",
    "ru":"<code>Это может занять некоторое время, пожалуйста, пожалуйста... 🖐</code>",
    'en':"<code>This may take some time please wait ... 🖐</code>"
}
