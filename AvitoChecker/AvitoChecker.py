import telebot
import random
import time
import requests
import cfscrape
import lxml

from bs4 import BeautifulSoup
from telebot import types

DEBUG = False

TOKEN = '1262884038:AAH9rbl53THU28HzMn9Vo9dMTipPwE_syoU'
bot = telebot.TeleBot(TOKEN)

users = ['484338199'] #, '0']
urls = [
    {
        'url': 'https://www.avito.ru/rossiya/avtomobili?cd=1&proprofile=1',
        'alias': 'все машины',
        'new_data': False,
        'data': None
    },
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2104-ASgBAgICAkTgtg3GmSjitg3Imig',
        'alias': 'пятёрки',
        'new_data': False,
        'data': None
    },
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2104-ASgBAgICAkTgtg3GmSjitg3Imig',
        'alias': 'шестёрки',
        'new_data': False,
        'data': None
    }
]


#@bot.message_handler() ID
#def sas(message):
#    print(message.chat.id)
#    return

def parsePage(text):
    soup = BeautifulSoup(text,'lxml')
    link = soup.find('div', class_ = 'snippet').find('div', class_= 'item__line').find('div', class_='item-photo').find('a',class_='item-slider').get('href')
    return link

def checkAvito():
    scraper = cfscrape.create_scraper()      
   
    #for url in urls:
    #    print(f'Checking for updates ({url["alias"]})')
        
    #    page = scraper.get(url["url"]).text
        
    #    #getContent(page)
    #    #if not page.status_code == 200:
    #    #    print(f'Something went wrong during loading page (code: {page.status_code})')

    #    time.sleep(0.25)
    page = scraper.get(urls[0]["url"]).text
    link = parsePage(page)
    msg = f'Новое объявление!\nhttps://www.avito.ru{link}'
    print(f'Sending: {msg}')
    bot.send_message(users[0], msg)
    return

def Routine():
    while (True):
        print('Checking updates..')
        checkAvito()
        #if newData:
        #    print('New advert(s) found, beautifying data..')
        #    beautifyData()
        #    for user in users:
        #        print(f'Sending beautified advert to {user}')
        #        bot.send_message(user, 'test')
        time.sleep(60)
    return

def main():
    if not DEBUG:
        try:
            Routine()
        except Exception:
            print("Runtime exception occuried")
            main()
    else:
        Routine()
    return

# RUN
#bot.polling(none_stop=True)

if __name__ == '__main__':
    main()