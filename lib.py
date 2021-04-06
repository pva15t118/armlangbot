import telebot
from user import User as u
import requests
from datetime import datetime
import time
import sys

token = '1106503066:AAGJgygRq14Y2YQc3g5hkuAcqdkrsiewaMo'
conn_retry, retry_interval = 6, 3

bot = telebot.TeleBot(token)


def start():

    @bot.message_handler(commands=['start'])
    def example(m):
        u_id = m.chat.id
        u_name = 'UserNmae'
        u(u_id, u_name).create()

    bot.polling()


def prepare():
    # print('Приветствие')
    # print('Проверка соединения...')
    # отправляем какой-нибудь запрос к апи, просто так

    # print('Проверка соединения с базой...')
    # отправляем запрос в базу, либо чекаем коннекшон

    # print('Ура, заработало! Приложенька, версия, авторы и тд')
    print()


if __name__ == '__main__':
    print(f'[StartedSession] {datetime.now()}')
    prepare()
    print()
    retr = 0
    while retr < conn_retry:
        retr += 1
        #
        try:
            start()
        except Exception as ex:
            if retr == 1:
                print(datetime.now(), 'Error:')
                for a in ex.args:
                    print(a)
            else:
                console_msg = f'Retry: {retr} ...'
                sys.stdout.write(console_msg)
                sys.stdout.flush()
                time.sleep(retry_interval)
                sys.stdout.write('\b' * len(console_msg))
            continue
    retry_off_msg = f'Unable to restart session. ' \
                    f'Max Retry Limit: {conn_retry}, ' \
                    f'Interval: {retry_interval} sec'

    print('-' * len(retry_off_msg))
    print(retry_off_msg)
    print('-' * len(retry_off_msg))

    print('Press enter to quit')
    i = str(input())
