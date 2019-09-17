"""
Оффлайн задание №2

Реализуйте в боте команду /wordcount которая считает слова в присланной фразе. Например на запрос /wordcount Привет как дела бот должен ответить: 3 слова. Не забудьте:

Добавить проверки на пустую строку
Как можно обмануть бота, какие еще проверки нужны?

"""

'''Done! Congratulations on your new bot. You will find it at t.me/wcb_lsv_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
760986984:AAEYD_IeLyyhRWlClj5YT2k0FZ3jSKlz2gw
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api'''

import ephem
import logging
import re
import ephem

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

def wordcount(bot, update):
    text_0 = update.message.text[11:]
    print(text_0)

    if text_0 != '':
        regex = r'[\s]'
        wlist = re.split(regex, text_0)
        print(wlist)
        update.message.reply_text(f'Количество слов в сообщении: {len(wlist)}')
    else:
        update.message.reply_text('Вы ввели пустую строку.')

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def when_full_moon(bot, update):
    user_text = update.message.text
    print(user_text)
    dt = user_text.split()[1]
    answ = str(ephem.next_full_moon(dt))
    update.message.reply_text(str(answ))

def main():
    mybot = Updater("760986984:AAEYD_IeLyyhRWlClj5YT2k0FZ3jSKlz2gw", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", when_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    print('*' * 10)

if __name__ == "__main__":
    main()
