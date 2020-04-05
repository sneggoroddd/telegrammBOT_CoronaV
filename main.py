import  COVID19Py
import telebot





from telebot import apihelper

PROXY = 'socks5://154.16.63.16:1080'

apihelper.proxy = {'https': PROXY}

TOKEN = '1175013152:AAE1wYUd3L7NE6RBs7zYXqwks4Ow5XA4m5c'

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)


#latest = covid19.getLatest()
# print(latest)
#location = covid19.getLocationByCountryCode("Ru")

# print(latest)
# print(location)