import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "7355070235:AAGYpwE53hirX7eBEAJMiJHVhq8_TJvC1So"
WEB_APP_URL = "https://vm3784024.stark-industries.solutions"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Рассчитать стоимость номера", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)
    bot.send_message(message.chat.id, "Привет! Нажмите кнопку ниже, чтобы рассчитать стоимость номера.", reply_markup=keyboard)

bot.polling()
