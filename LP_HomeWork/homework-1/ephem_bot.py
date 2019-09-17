"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem +
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""

'''
сообщение от BotFather:
Done! Congratulations on your new bot. You will find it at t.me/ephem_user_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
699053794:AAH8KEIug-7IZXTSlUOMQGfFEq_oyrVPQtk
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api'''

import ephem
import logging
import datetime

now = datetime.datetime.now()
dt = '{:04}/{:02}/{:02}'.format(now.year, now.month, now.day)

print(dt)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet_take(bot, update):
    text_0 = update.message.text
    print(text_0)
    text_2 = text_0.split()[1].capitalize()
    print(text_2)
    update.message.reply_text(text_2)

    print('planets passed')

    if text_2 in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Titan']:
        p = ephem.constellation(getattr(ephem, text_2)(dt))[1]
        update.message.reply_text(str(p))
        print('----------')

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("699053794:AAH8KEIug-7IZXTSlUOMQGfFEq_oyrVPQtk", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_take))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    print('*'*10)
    mybot.start_polling()
    mybot.idle()
    print('*' * 10)

if __name__ == "__main__":
    main()
