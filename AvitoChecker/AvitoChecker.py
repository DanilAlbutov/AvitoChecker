import telebot
import Config
import random
import time
import requests
import cfscrape
import lxml
from bs4 import BeautifulSoup
from telebot import types



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


#@bot.message_handler()
#def sas(message):
#    print(message.chat.id)
#    return

def parsePage(text):
    try:
        soup = BeautifulSoup(text,'lxml')
        items = soup.find('div', class_ = 'snippet').find('div', class_= 'item__line').find('div', class_='item-photo').find('a',class_='item-slider').get('href');
        #for item in items:
        print(items)
        #container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        #url_block = container[0].select('a.item-slider item-slider--1-1')
        #url_block = item.select_one('a.item-slider item-slider--1-1')
        #href = url_block.get('href')   
        #print(href)
    except Exception:
        print(f'exception: {Exception}')

    return

def getContent(html):
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find('div', class_ = 'snippet snippet-horizontal')
    link = link.find('a').get('href')
    print(link)


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
    parsePage(page)
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