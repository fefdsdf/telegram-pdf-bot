import telebot

# Вставляем свой токен
TOKEN = '8038337871:AAEwLHtM_4WSTzDUb6B-zdOQW-ecelYsVpQ'

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
        "Привет! 👋 Я бот, который отправит тебе полезный PDF.\nНапиши /buy чтобы получить файл.")

# Команда /buy — отправляет PDF
@bot.message_handler(commands=['buy'])
def send_pdf(message):
    with open('guide.pdf', 'rb') as file:
        bot.send_document(message.chat.id, file, caption="📘 Вот твой гайд! Удачи!")

# Запуск бота
bot.polling()
