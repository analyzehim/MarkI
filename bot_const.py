#!/usr/bin/env python
# -*- coding: utf-8 -*- 



INTERVAL = 3 # Sec interval between checkhing update
ADMIN_ID = 74102915 # My ID
PIG_ID = 117797858 # Anna Scherbakova
URL = 'https://api.telegram.org/bot' # HTTP Bot API URL
#TOKEN = '119170444:AAGu9QuWoZ7WFAIQS-1q1Az4rhzHQdiFfDk' # My Token
PATTERN_DICE = '/\d*d\d*'# Reg mask for dice
PIG_LIST = ['cute','adorable','attractive','beautiful','handsome','pretty','gorgeous','lovely','foxy','sexy','hot','babe'] 
CHAT_ID = 65

def parseConfig():
    f = open("client.txt",'r')
    for line in f:
        return line


def checkMode():
    proxies = getProxies()
    return 0

def getProxies():
    f = open("proxy.txt","r")
    proxy_url = f.read()
    f.close()

    proxies = {
      "http": proxy_url,
      "https": proxy_url,
    }
    return proxies

def checkMode():
    import requests
    proxies = getProxies()
    try:
            request = requests.get('https://www.ya.ru')
            return 1
    except:
            request = requests.get('https://www.ya.ru',proxies = proxies)
            return 0
    return -1

