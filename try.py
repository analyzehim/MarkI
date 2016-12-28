'''
import sqlite3
from common_proto import *
con = sqlite3.connect('data/life/life.db')
cur = con.cursor()


left = 1482872400
right = 1482958800
def get_stat_from_bd(left, right):
    mas = []
    for row in cur.execute('SELECT * FROM LIFE WHERE date >{0} and date <{1}'.format(left, right)):
        mas.append([row[2],row[1]])

    mas = sorted(mas ,key=lambda x: x[0])
    stat=''
    for i in mas:
        stat+= human_time(i[0]).split(' ')[1]+'  ' + i[1]+'\n'
    return stat

print get_stat_from_bd(left, right)


timestamp = float(time.time())
print timestamp
print 1, human_time(1482899894)

print datetime.datetime.fromtimestamp(timestamp)

print 1, get_unixtime(28,12,2016,8,5)



import sqlite3
import datetime
import time
import random
con = sqlite3.connect('data/life/life1.db')
cur = con.cursor()


def human_time(time):
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

def pip(st):
    import os
    f = open("password.txt", "r")
    password = f.read()
    pip_str ='pip install {0} --proxy "KL\Raev_e:{1}"@proxy.avp.ru:8080'.format(st, password)
    os.system(pip_str)
    return 1



import sqlite3
from math import sqrt
import glob
import time
con = sqlite3.connect('data/life/life.db')
cur = con.cursor()
def init():
    cur.execute()
init()




CREATE TABLE IF NOT EXISTS `tbl` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
  `name` varchar(255) NOT NULL);
CREATE TABLE `T` (
	`id`	INTEGER,
	`name`	VARCHAR(100),
	`date`	INTEGER,
	`price`	REAL,
	`day_return`	REAL,
	PRIMARY KEY(id)
);
import xml.etree.ElementTree as ET
tree = ET.parse('config')
root = tree.getroot()
proxy = root.findall('proxy')[0].text
token = root.findall('token')[0].text


f = open("proxy.txt","r")
proxy_url = f.read()
f.close()

proxies = {
  "http": proxy_url,
  "https": proxy_url,
}


import http.client
conn = http.client.HTTPConnection("lectureswww.readthedocs.org")
conn.request("GET", "/ru/latest/")
r1 = conn.getresponse()
print(r1.status)

URL = 'https://api.telegram.org/bot' # HTTP Bot API URL
TOKEN = '119170444:AAGu9QuWoZ7WFAIQS-1q1Az4rhzHQdiFfDk' # My Token
#data1 = json.loads('"text": "Hello","chat_id": 74102915,"reply_markup":{"keyboard":[["0"],["1"]], "one_time_keyboard":true}')


#data = {'chat_id': 74102915, 'text': 1} # Request create

#print data, URL + TOKEN + '/sendMessage'

data = {'text': 1, 'chat_id': 74102915, 'reply_markup':{'keyboard':[ [ "Top Left", "Top Right" ], [ "Bottom Left", "Bottom Right" ] ],'one_time_keyboard':True}}
data1 = json.dumps(data)
data1 = {"text":1, "chat_id": 74102915, "reply_markup":{"keyboard":[["0"],["1"]], "one_time_keyboard":True} }

#r =  requests.post(URL + TOKEN + '/sendMessage',json=data1, proxies=proxies)
#print data1
#print r.content

class A:
    def __init__(self):
        self.example = 2
    def func(self):
        return self.a


a = A()
print a.func()
'''