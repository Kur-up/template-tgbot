import os
import time
import configparser

import telebot

import modules.module_database_postgresql as m_db_psql


config = configparser.ConfigParser()
config_path = os.path.join(os.getcwd(), 'config.ini')
config.read(config_path)
telegram_bot_token = str(config['General']['tg_bot_token'])

m_db_psql.initialization()

while True:
    try:
        telegram_bot = telebot.TeleBot(telegram_bot_token)
    except Exception as exc:
        print('[ERROR] - Bot initialization failed!')
        print(exc)
        time.sleep(1)
    else:
        break


@telegram_bot.message_handler(commands=['start'])
def handler_start_command(message):
    telegram_bot.delete_message(message.from_user.id, message.id)


@telegram_bot.message_handler(content_types=['text'])
def handler_message(message):
    telegram_bot.delete_message(message.from_user.id, message.id)
    if message.text == 'text1':
        pass
    elif message.text == 'text2':
        pass
    else:
        telegram_bot.delete_message(message.from_user.id, message.id)


@telegram_bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "callback1":
        pass
    elif call.data == "callback2":
        pass
    else:
        pass


telegram_bot.polling(none_stop=True, interval=0)
