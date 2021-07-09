import random
from time import sleep
from random import randint
from const import *
import time
def start(update,context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=user_id,text='Привет {}'.format(name))
    datatime = time.asctime()
    Logpath = 'file.txt'
    log = open(Logpath, 'a')
    logstr = "{} | {}: {}\n".format(datatime, "123", '/start')
    log.writelines(logstr)

def text_answer(update, context):
    user_id = update.message.chat_id
    text = update.message.text
    text = text.lower()
    number = update.message.text
    if text in DCT.keys():
        context.bot.send_message(chat_id = user_id, text = (DCT.get(text)))
        datatime = time.asctime()
        Logpath = 'file.txt'
        log = open(Logpath, 'a')
        logstr = "{} |сообщение которое было отправленно ботом: {}\n".format(datatime,(DCT.get(text)))
        log.writelines(logstr)
    else:
        datatime = time.asctime()
        Logpath = 'file.txt'
        log = open(Logpath, 'a')
        logstr = "{} | user id:{}, Что возможно надо добавить в команду:{}\n".format(datatime, user_id, text)
        log.writelines(logstr)
        log.close()

        if number == my_number:
            context.bot.send_message(chat_id=user_id, text=f"Ты угадал мое число! {my_number}")
        else:
            context.bot.send_message(chat_id=user_id, text="Ты не угадал мое число")

