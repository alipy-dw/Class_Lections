import telebot
from telebot import types
from bs4 import BeautifulSoup as bs
import requests

bot = telebot.TeleBot('7845548903:AAHv12ee5Ey50Yg1-2fvgGJb5yOjI7tGUSw')
keybord = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = types.KeyboardButton('Спарсить Ноутбуки')
button2 = types.KeyboardButton('Спарсить Телефоны')
keybord.add(button1,button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, я делаю парсинг товаров сайта Kivano.kg!', reply_markup=keybord)
    bot.register_next_step_handler(message2, hendler)

@bot.message_handler(content_types=['text'])
def hendler(message):
    if message.text == 'Спарсить Телефоны':
        parsing_phone('https://www.kivano.kg/mobilnye-telefony', message)
    elif message.text == 'Спарсить Ноутбуки':
        parsing_laptop('https://www.kivano.kg/noutbuki-i-kompyutery', message)
    else:
        bot.send_message(message.chat.id, "Нажмите на кнопку!", reply_markup=keybord)

def parsing_laptop(url, message):
    html = requests.get(url).text
    soup = bs(html, 'lxml')
    laptops = soup.find_all('div', class_="item product_listbox oh")
    count = 1
    for laptop in laptops:
        title = laptop.find('img').get('alt')
        link = 'https://www.kivano.kg' + laptop.find('a').get('href')
        price = laptop.find('div', class_="listbox_price text-center").find('strong').text
        bot.send_message(message.chat.id, f'{count}) Ноутбук - {title}\nЦена - {price}\nСсылка - {link}')
        count += 1

def parsing_phone(url, message):
    html = requests.get(url).text   
    soup = bs(html, 'lxml')
    phones = soup.find_all('div', class_="item product_listbox oh")
    for phone in phones:
        link = 'https://www.kivano.kg' + phone.find('a').get('href')
        title = phone.find('img').get('alt')
        price = phone.find('div', class_="listbox_price text-center").find('strong').text
        bot.send_message(message.chat.id, f'Телефон - {title}\nЦена - {price}\nСсылка - {link}')


bot.polling(non_stop=True, interval = 0)