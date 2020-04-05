import telebot
from telebot import apihelper


TOKEN = '1183654282:AAHWVQVulVPx4RLFD067Nu6dlaHj7SSbsqA'
from telebot import apihelper

PROXY = 'socks5://154.16.63.16:1080'
apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(content_types=['text'])
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'В тексте слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)

bot.polling(none_stop=True)