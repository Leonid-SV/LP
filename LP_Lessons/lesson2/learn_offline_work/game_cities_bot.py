"""
Оффлайн задание №2

Научите бота играть в города. Правила такие - внутри бота есть список городов, пользователь пишет /cities Москва и если в списке такой город есть, бот отвечает городом на букву "а" - "Альметьевск, ваш ход". Оба города должны удаляться из списка.

Помните, с ботом могут играть несколько пользователей одновременно
"""

'''Use this token to access the HTTP API:
679833706:AAGhns_dbi441rvpXhQSnnXLAP5BaN1W1fg
Keep your token secure and store it safely, it can be used by anyone to control your bot.'''

import logging
import re
import cities

# считывает из файла названия городов России и записывает в словарь вида {Номер: Название}
cities.read_cities_csv()


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

def cities_game(bot, update):

    text_0 = update.message.text[8:]
    a = cities.cities(text_0)
    update.message.reply_text(f'{a}')

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("679833706:AAGhns_dbi441rvpXhQSnnXLAP5BaN1W1fg", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cities", cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    print('*' * 10)

if __name__ == "__main__":
    main()
