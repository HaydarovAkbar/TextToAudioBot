import datetime
# from gtts import gTTs
from Battons import *
from database import DataBase


nowD = datetime.datetime.now()
date = nowD.strftime("%Y/%m/%d %H:%M")
db = DataBase()

def russ(update,context):
    text = update.message.text
    tts = gTTS(text=text, lang="ru",slow="False")
    tts.sav("Russ.mp3")
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open("D:\Zako_New_project\TextAudioBOT\Russ.mp3","rb"),
                           reply_markup=backBattton)

def ingliz(update,context):
    text = update.message.text
    tts = gTTS(text=text, lang="en",slow="False")
    tts.sav("Ingliz.mp3")
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open("D:\Zako_New_project\TextAudioBOT\Ingliz.mp3","rb"),
                           reply_markup=backBattton)
def ovoz(update,context):
    text = update.message.text
    bol = False
    for i in rus:
        if i in text:
            bol = True
            break
    if bol:
        return russ(update,context)
    else:
        return ingliz(update,context)


def admin(update,context):
    baza = db.getBasa()
    base = "⛔️<b>Botdan foydalanuvchilar haqida maxfiy</b> 🔐 malumotlar!\n\n"
    c = 1
    for i in baza:
        base += f"{c}.<b>{i[2]}</b> ismli foydalanuvchi     🕒: <b>{i[3]}</b> 👈   vaqtda botga qushilgan✅    🇺🇿Tg: @{i[1]}\n"
        c += 1
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"{base}",
                             parse_mode = "HTML",
                             reply_markup = backAkbar)

def tekshir(update,context):
    user = update.message.from_user
    userN,firstN,dat,ID = user.username,user.first_name,date,user.id
    a = db.getBaseID(user.id)
    if not a:
        db.setBase(userN,firstN,dat,ID)

def start(update,context):
    user = update.message.from_user
    tekshir(update,context)
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"{user.first_name}❇️ <b>Bot</b> orqali siz: ❇️\n"
                                                                        f"\n📝 <b>Text</b> ko'rinishidagi malumotni\n"
                                                                        f"\n🔊 <b>Audio</b> ko'rinishiga o'tkazishingiz mumkin\n"
                                                                        f"\n🆕Bot imkoniyatlariga yana reklama tarqatish ham qo'shilgan 🆓\n"
                                                                        f"\n  ✳️✳️Reklama uchun <b>dasturchi</b> bilan aloqaga chiqing ✳️✳️\n"
                                                                        f"\n👇 Quyidagilardan birini tanlang ✅",
                             parse_mode = "HTML",
                             reply_markup = startBatton)
def userCount(update,context):
    soni = len(db.getBasa())
    s = ""
    for i in str(soni):
        s += sonlar.get(i,i)

    context.bot.send_message(chat_id = update.effective_chat.id, text = f"🤖<b>BOT</b>dan foydalanuvchilar soni 👉 {s} ta",
                             parse_mode = "HTML",
                             reply_markup = backBattton)

def material(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"✋ <b>Siz fikrlaringizni</b> (#FIKR ...)✅\n "
                                                                        f"\n🔹 Ko'rinishida yuboring man uni albatta "
                                                                        f"dasturchiga yetkazaman!\n"
                                                                        f"\n#️⃣ Masalan: #FIKR Bu bot nimaga kerak❓🤨",
                             parse_mode = "HTML",
                             reply_markup = backBattton)

def programmer(update,context):
    user = update.message.from_user
    if user.id == 758934089:
        context.bot.send_message(chat_id = 758934089, text = f"🔥 Assalomu alaykum <b>Akbar</b>!🔥 \n\n🌏<i>Botingizga xush kelibsiz</i>!🌏",
                                 parse_mode = "HTML",
                                 reply_markup = akbarBatton)
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"Dasturchi haqida malumot:\n"
                                                                            f"\n👨‍💻 <b>Haydarov Akbar</b> <i>Python</i> and <i>Django</i> developer\n"
                                                                            f"\n🇺🇿Telegram: @Akbar_TUIT",
                                 parse_mode = "HTML",
                                 reply_markup = backBattton)
def fikr(update,context):
    text = update.message.text
    user = update.message.from_user
    context.bot.send_message(chat_id=758934089, text=f"💬 Sizga {user.first_name} tominidan fikr qoldirildi\n\n"
                                                     f"🇺🇿 Telegram @{user.username} \n\n{text}", )

def reklama(update,context):
    text = update.message.text
    base = db.getBasa()
    for j in base:
        context.bot.send_message(chat_id = j[4], text = text)

def orqagaStart(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"♻️ Quyidagilardan birini tanlang 👇✅",
                             parse_mode="HTML",
                             reply_markup=startBatton)

def main(update,context):
    text = update.message.text
    user = update.message.from_user
    if text == "📝 Textni audioga o'zgartirish 🔊":
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"❇️ <b>{user.first_name}</b> Botga: \n\n🇬🇧 <i>Ingliz tili</i>\n🇷🇺 <i>Rus tili</i>\n\nKo'rinishidagi "
                                                                            f"textlarni yuborishingiz mumkin \n🔉 Bot sizga "
                                                                            f"<b>audio</b> ko'rinishida qaytaradi\n\n"
                                                                            f"👨‍🔧 Agarda <b>text</b> uzunroq bo'lsa <b>audio</b> biroz kechikishi mumkin 🏎",
                                 parse_mode = "HTML",
                                 reply_markup = backBattton)
    elif text == "🔙 Orqaga 🔙":
        return orqagaStart(update,context)

    elif text == "🚫 Orqaga qaytish🚫":
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"👇 Quyidagilardan birini tanlang <b>Akbar</b>",
                                 parse_mode="HTML",
                                 reply_markup=akbarBatton)

    elif text == "🙋‍♂️Foydalanuvchilar soni 💁‍♂️":
        return userCount(update,context)

    elif text == "🤖 Bot Foydalanuvchilari 🤖":
        return admin(update,context)

    elif text == "❇️ Reklama 🌉":
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"📸 <b>Reklama</b> tarqatish uchun siz 📳(#NEW) "
                                                                            f"so'zini <b>bot</b>ga yuborishingiz kerak",
                                 parse_mode = "HTML",
                                 reply_markup = backAkbar)
    elif "#NEW" in text:
        return reklama(update,context)

    elif "#FIKR" in text:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "✅ <b>Fikringiz uchun rahmat</b>❗️😊",
                                 parse_mode = "HTML",
                                 reply_markup = backBattton)
        return fikr(update,context)

    elif text == "🤖 Fikr qoldirish 📌":
        return material(update,context)

    elif text == "👨‍💻 Dasturchi 📞":
        return programmer(update,context)

    else:
        return ovoz(update,context)
