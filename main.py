# -*- coding: utf-8 -*-
import requests
import time
import subprocess
import os
#import mailchecker
import random
import re
from bot_proto import *
from bot_const import *
from bot_vk import *

def check_updates():
    global offset
    data = {'offset': offset + 1, 'limit': 5, 'timeout': 0} # Формируем параметры запроса
    
    try:
        request = requests.post(URL + TOKEN + '/getUpdates', data=data) # Отправка запроса обновлений
    except:
        log_event('Error getting updates') # Логгируем ошибку
        return False # Завершаем проверку
    if not request.status_code == 200: return False # Проверка ответа сервера

    if not request.json()['ok']: return False # Проверка успешности обращения к API
    
    for update in request.json()['result']: # Проверка каждого элемента списка
        offset = update['update_id'] # Извлечение ID сообщения

        if not 'message' in update or not 'text' in update['message']: continue

        from_id = update['message']['chat']['id'] # Chat ID
        author_id = update['message']['from']['id'] # Creator ID
        message = update['message']['text'] 
        try:
            name = update['message']['chat']['first_name'] # Извлечение username отправителя      
        except:
            name = update['message']['from']['first_name'] 

        parameters = (offset, name, from_id, message, author_id)
        try:
            log_event('Message (id%s) from %s (id%s): "%s" with author: %s' % parameters) 
        except:
            pass
        run_command(*parameters)


def run_command(offset, name, from_id, cmd, author_id):
    if cmd == '/ping':
        send_text(from_id, 'pong') 

    elif cmd == '/help':
        send_text(from_id, 'No help today. Sorry, %s'%name)

    elif cmd in ('Hello','hello','hi','Hi'): # Say hello
        send_text(from_id, 'Hello, %s'%name)

    elif cmd == '/pig' and author_id in (ADMIN_ID, PIG_ID): 
        send_text(from_id, 'Pig is '+random.choice(PIG_LIST)) # Answer

    elif cmd =='/vk' and author_id in (ADMIN_ID, PIG_ID) :
        del_mes = 0
        for i in range(1):
            del_mes+=delete_mes(200,0)
            del_mes+=delete_mes(200,200)
        send_text(from_id,'Deleting %s messages' % str(del_mes) )

    elif cmd == '/photo': # Запрос фотографии с подключенной Web-камеры
        # Для оператора If ниже. Если первая попытка успешна - выполняется условие, если нет, то вторая попытка и условие
        # Если и вторая не успешна, тогда отчитываемся об ошибке
        # Всё потому, что на моей конфигурации крайне изредка камера бывает недоступна с первого раза
        if make_photo(offset) or make_photo(offset):
            # Ниже, отправка пользователю уведомления об активности бота
            requests.post(URL + TOKEN + '/sendChatAction', data={'chat_id': from_id, 'action': 'upload_photo'})
            send_photo(from_id, offset) # Вызов процедуры отправки фото
        else:
            send_text(from_id, 'Error occured') # error answer

    elif cmd == '/keyboard':
        keyboardLayout = [["they're okay", "I LOVE THEM"]]
        reply_markup={"keyboard":[["Yes","No"],["Maybe"],["1","2","3"]],"one_time_keyboard":True}
        messageText='Kyeyboard OK'
        data = {'chat_id': from_id, 'text': messageText, 'reply_markup': reply_markup}
        requests.get(URL + TOKEN + "/sendMessage", data=data)



    elif re.match(PATTERN_DICE,cmd) is not None:
        number = int( cmd.split('d') [0] [1:] )
        dice_size = int( cmd.split('d') [1] )
        if dice_size < 2 or number < 1:
                send_text(from_id, '%s, wrong input :C' %name)
                return
        print 1
        send_text(from_id, "Result: " + str( [ random.randint(1,dice_size) for i in range(number) ] ) )
    else:
        pass
        #send_text(from_id, 'What?')


if __name__ == "__main__":
    while True:
        try:
            check_updates()
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
