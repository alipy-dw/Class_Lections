import telebot
from telebot import types as tp
bot = telebot.TeleBot('7845548903:AAHv12ee5Ey50Yg1-2fvgGJb5yOjI7tGUSw')

keyboard = tp.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = tp.KeyboardButton('Snow me what i wrote, bitchyoASS')
keyboard.add(button1)

@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Hello,if you try write some bad words, you gone take responsible, and pay back')
    bot.register_next_step_handler(message, save_info)
 
def save_info(message):
    try:
        with open('user_info.txt', 'a') as file:
            info = message.text
            file.write(info+'\n')
    except:
        bot.send_message(message.chat.id, 'Something gone wrong')
    else:
        bot.send_message(message.chat.id, 'everything saved!!!', reply_markup=keyboard)
    finally:
        print('OK')

@bot.message_handler(content_types=['text'])
def send_info(response):
    if response.text == 'Snow me what i wrote, bitchyoASS':
        with open('/home/hello/Рабочий стол/Class lections/telegramm_bot/user_info.txt') as file:
            bot.send_document(response.chat.id, file)
    else:
        bot.send_message(response.chat.id, 'Press the button', reply_markup=keyboard)
bot.polling(non_stop=True, interval=0)