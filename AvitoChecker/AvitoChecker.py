import telebot
import Config
import random
import time
import requests
import cfscrape

from telebot import types
from bs4 import BeautifulSoup

TOKEN = '1262884038:AAH9rbl53THU28HzMn9Vo9dMTipPwE_syoU'
bot = telebot.TeleBot(TOKEN)

cd = 1;
searchRadius = 100;
# ?cd=1&radius=100

users = ['484338199'] #, '0']
urls = [
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2104-ASgBAgICAkTgtg3GmSjitg3Imig',
        'alias': 'четвёрки',
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


#@bot.message_handler()
#def sas(message):
#    print(message.chat.id)
#    return


def checkAvito():
    scraper = cfscrape.create_scraper()      
   
    for url in urls:
        print(f'Checking for updates ({url["alias"]})')
        
        page = scraper.get(url["url"]).content
        #if not page.status_code == 200:
        #    print(f'Something went wrong during loading page (code: {page.status_code})')

        time.sleep(0.25)
    return

def beautifyData():
    return

def main():
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
  
# RUN
#bot.polling(none_stop=True)

if __name__ == '__main__':
    main()