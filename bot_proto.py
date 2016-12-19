# -*- coding: utf-8 -*-
import requests
import time
import subprocess
import os
import json
import random
import re
from bot_const import *
requests.packages.urllib3.disable_warnings() # Подавление InsecureRequestWarning, с которым я пока ещё не разобрался



def log_event(text):
    """
    Logging
    """
    f = open('log.txt', 'a')
    event = '%s >> %s' % (time.ctime(), text)
    f.write(event+'\n')
    f.close()
    print event

def send_text_withKeyboard(chat_id, text, keyboard):
    try:
        log_event('Sending to %s: %s; keyboard: %s' % (chat_id, text, keyboard)) # Logging
    except:
         log_event('Error with LOGGING')
    json_data = {"chat_id":chat_id, "text": text, "reply_markup":{"keyboard":keyboard, "one_time_keyboard":True} }
    print json_data

    request = requests.post(URL + TOKEN + '/sendMessage', json=json_data) # HTTP request
    if not request.status_code == 200: # Check server status
        return False 
    return request.json()['ok'] # Check API

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
