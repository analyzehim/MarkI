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


class Telegram:
    def __init__(self):
        self.TOKEN = parseConfig()
        self.URL = 'https://api.telegram.org/bot'
        self.mode = checkMode()
        self.proxies = getProxies()
        self.chat_id = 74102915
        self.offset = 0
        self.Interval = 0.5

    def get_updates(self):
        data = {'offset': self.offset + 1, 'limit': 5, 'timeout': 0}
        if self.mode == 1:
            request = requests.post(URL + TOKEN + '/getUpdates', data=data)
        if self.mode == 0:
            request = requests.post(self.URL + self.TOKEN + '/getUpdates', data=data, proxies = self.proxies)
        return request

    def send_text_withKeyboard(self, chat_id, text, keyboard):
        try:
            log_event('Sending to %s: %s; keyboard: %s' % (chat_id, text, keyboard)) # Logging
        except:
             log_event('Error with LOGGING')
        json_data = {"chat_id":chat_id, "text": text, "reply_markup":{"keyboard":keyboard, "one_time_keyboard":True} }
        if self.mode == 1: #no proxy
            request = requests.post(self.URL + self.TOKEN + '/sendMessage', json=json_data) # HTTP request

        if self.mode ==0:
            request = requests.post(self.URL + self.TOKEN + '/sendMessage', json=json_data, proxies = self.proxies) # HTTP request with proxy 

        if not request.status_code == 200: # Check server status
            return False 
        return request.json()['ok'] # Check API

    def send_text(self, chat_id, text):
        """Send text message by chat_id"""
        try:
            log_event('Sending to %s: %s' % (chat_id, text)) # Logging
        except:
             log_event('Error with LOGGING')
        data = {'chat_id': chat_id, 'text': text} # Request create
        if self.mode ==1:
            request = requests.post(self.URL + self.TOKEN + '/sendMessage', data=data) # HTTP request

        if self.mode ==0:
            request = requests.post(self.URL + self.TOKEN + '/sendMessage',  data=data, proxies = self.proxies) # HTTP request with proxy 

        if not request.status_code == 200: # Check server status
            return False 
        return request.json()['ok'] # Check API
    def ping(self):
        data = {'chat_id': self.chat_id, 'text': 'ping'}
        if self.mode ==1:
            request = requests.post(self.URL + self.TOKEN + '/sendMessage', data=data) # HTTP request

        if self.mode ==0:
            request = requests.post(self.URL + self.TOKEN + '/sendMessage',  data=data, proxies = self.proxies) # HTTP request with proxy 





def log_event(text):
        """
        Logging
        """
        f = open('log.txt', 'a')
        event = '%s >> %s' % (time.ctime(), text)
        print event + '\n'
        #f.write(event+'\n')
        f.close()
        print event
