# -*- coding: utf-8 -*-
import requests
import time
import subprocess
import os
#import mailchecker
import random
import re
from bot_const import *
requests.packages.urllib3.disable_warnings() # Подавление InsecureRequestWarning, с которым я пока ещё не разобрался

# Ключ авторизации Вашего бота Вы можете получить в любом клиенте Telegram у бота @BotFather
# ADMIN_ID - идентификатор пользователя (то есть Вас), которому подчиняется бот
# Чтобы определить Ваш ID, я предлагаю отправить боту сообщение от своего имени (аккаунта) через любой клиент
# А затем получить это сообщения с помощью обычного GET запроса
# Для этого вставьте в адресную строку Вашего браузера следующий адрес, заменив <token> на свой ключ:
# https://api.telegram.org/bot<token>/getUpdates
# Затем, в ответе найдите объект "from":{"id":01234567,"first_name":"Name","username":"username"}
# Внимательно проверьте имя, логин и текст сообщения
# Если всё совпадает, то цифровое значение ключа "id" - это и есть ваш идентификатор

# Переменным ADMIN_ID и TOKEN необходимо присвоить Вашим собственные значения


def log_event(text):
    """
    Logging
    """
    f = open('log.txt', 'a')
    event = '%s >> %s' % (time.ctime(), text)
    f.write(event+'\n')
    f.close()
    print event

def send_text(chat_id, text):
    """Send text message by chat_id"""
    try:
        log_event('Sending to %s: %s' % (chat_id, text)) # Logging
    except:
         log_event('Error with LOGGING')
    data = {'chat_id': chat_id, 'text': text} # Request create
    request = requests.post(URL + TOKEN + '/sendMessage', data=data) # HTTP request
    if not request.status_code == 200: # Check server status
        return False 
    return request.json()['ok'] # Check API
'''
def make_photo(photo_id):
    """Обращение к приложению fswebcam для получения снимка с Web-камеры"""
    photo_name = 'photo/%s.jpg' % photo_id # Формирование имени файла фотографии
    subprocess.call('fswebcam -q -r 1280x720 %s' % photo_name, shell=True) # Вызов shell-команды
    return os.path.exists(photo_name) # Проверка, появился ли файл с таким названием

def send_photo(chat_id, photo_id):
    """Отправка фото по его идентификатору выбранному контакту"""
    data = {'chat_id': chat_id} # Формирование параметров запроса
    photo_name = 'photo/%s.jpg' % photo_id # Формирования имени файла фотографии
    if not os.path.exists(photo_name): return False # Проверка существования фотографии
    files = {'photo': open(photo_name, 'rb')} # Открытие фото и присвоение
    request = requests.post(URL + TOKEN + '/sendPhoto', data=data, files=files) # Отправка фото
    return request.json()['ok'] # Возврат True или False, полученного из ответа сервера, в зависимости от результата
'''
