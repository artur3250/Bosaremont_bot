
import telebot
from config import BOT_TOKEN, GROUP_CHAT_ID
from google_sheets import append_to_sheet

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь мне своё имя, телефон и комментарий.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_data = message.text.split(",")
    if len(user_data) != 3:
        bot.send_message(message.chat.id, "Пожалуйста, введи данные в формате: Имя, Телефон, Комментарий")
        return

    name, phone, comment = [x.strip() for x in user_data]
    msg = f"Новая заявка:
Имя: {name}
Телефон: {phone}
Комментарий: {comment}"
    bot.send_message(GROUP_CHAT_ID, msg)
    append_to_sheet(name, phone, comment)
    bot.send_message(message.chat.id, "Спасибо! Ваша заявка принята.")

bot.polling()
