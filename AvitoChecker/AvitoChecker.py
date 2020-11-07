import telebot
import random
import time
import requests
import cfscrape
import lxml

from bs4 import BeautifulSoup
#from telebot import types

DEBUG = False

TOKEN = '1262884038:AAH9rbl53THU28HzMn9Vo9dMTipPwE_syoU'
bot = telebot.TeleBot(TOKEN)

isInited = None

users = ['484338199'] #, '0']
urls = [
    #{
    #    'url': 'https://www.avito.ru/ulyanovsk/avtomobili?radius=100&s=104&proprofile=1',
    #    'alias': 'все машины Ульяновск',
    #    'new_data': False,
    #    'data': None
    #},
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2104-ASgBAgICAkTgtg3GmSjitg3Imig?s=104',
        'alias': 'четверки',
        'new_data': False,
        'data': None
    },
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2106/i-19762006-ASgBAgICA0Tgtg3GmSjitg3Mmijqtg2wwig?s=104',
        'alias': 'шестёрки',
        'new_data': False,
        'data': None
    },
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2107-ASgBAgICAkTgtg3GmSjitg3Omig?s=104',
        'alias': 'семерки',
        'new_data': False,
        'data': None
    },
    {
        'url': 'https://www.avito.ru/ulyanovsk/avtomobili/vaz_lada/2105/i-19802011-ASgBAgICA0Tgtg3GmSjitg3Kmijqtg2uwig?s=104',
        'alias': 'пятерки',
        'new_data': False,
        'data': None
    }
]

#@bot.message_handler() 
#def sas(message):
#    print(message.chat.id)    
#    if message.text == 'startcheck' :
#        bot.send_message(message.chat.id, f'user with id:{message.chat.id} starting bot')
#        main()
#    return

def parsePage(text):
    soup = BeautifulSoup(text,'lxml')
    items = soup.find_all('div',class_='js-catalog-item-enum')
    cards = []
    for item in items:
        cards.append(
            {
                'last data':item.find('div', class_='snippet-date-info').get('data-tooltip'),
                'upgrade':item.find('div', class_ = 'styles-arrow-3WY7X'),
                'link':item.find('a', class_ = 'snippet-link').get('href')

            }
            )

    return f'https://www.avito.ru{cards[0]["link"]}'

def checkAvito():
    global isInited
    scraper = cfscrape.create_scraper()

    if not isInited:
        for url in urls:
            print(f'Setting last updated link for {url["alias"]}')
            page = scraper.get(url["url"]).text
            url['data'] = parsePage(page)
            url['new_data'] = False
            isInited = True
            time.sleep(5)
    else:
        for url in urls:
            print(f'Checking for updates ({url["alias"]})')
            page = scraper.get(url["url"]).text
            link = parsePage(page)

            if (url['new_data'] == False) and (link != url['data']):
                print(f'Found new car ({url["alias"]})! Adding it to a message queue..')
                url['new_data'] = True
                url['data'] = link

                msg = f'Новое объявление!\n{link}'
                print(f'Sending: {msg}')
                for user in users:
                    bot.send_message(user, msg)
            else:
                url['new_data'] = False

            time.sleep(5)
    return
  
def Routine():
    while (True):
        print('Checking updates..')
        checkAvito()
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

if __name__ == '__main__':
    for user in users:       
        bot.send_message(user, '-----Bot started working-----')
    isInited = False
    #bot.polling(none_stop=True)
    main()
