from telegram import ReplyKeyboardMarkup

startBatton = ReplyKeyboardMarkup([
    ["📝 Textni audioga o'zgartirish 🔊"],
    ["🙋‍♂️Foydalanuvchilar soni 💁‍♂️","🤖 Fikr qoldirish 📌"],
    ["👨‍💻 Dasturchi 📞"]
],resize_keyboard=True)

backBattton = ReplyKeyboardMarkup([
    ["🔙 Orqaga 🔙"]
],resize_keyboard=True)

backAkbar = ReplyKeyboardMarkup([
    ["🚫 Orqaga qaytish🚫"]
],resize_keyboard=True)

akbarBatton = ReplyKeyboardMarkup([
    ["🤖 Bot Foydalanuvchilari 🤖"],
    ["❇️ Reklama 🌉","🔙 Orqaga 🔙"],
],resize_keyboard=True)

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

a = {'update_id': 685923836,
     'message': {'message_id': 151, 'date': 1621938215,
                 'chat': {'id': 758934089, 'type': 'private', 'username': 'Akbar_TUIT', 'first_name': 'KH.Akbar'},
                 'text': '👨\u200d💻 Dasturchi 📞', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False,
                 'from': {'id': 758934089, 'first_name': 'KH.Akbar', 'is_bot': False, 'username': 'Akbar_TUIT', 'language_code': 'ru'}}}

rus = ["й","ц","у","к","ф","қ","ь","т","м","д","л","г","н","з","ж"]