import sqlite3
import datetime
import time
from common_proto import *
con = sqlite3.connect('data/life/life.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS `Life`
            (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
            `name` VARCHAR(100),
            `date` INTEGER);''')


def sqlite_add(st,date):
    print '''INSERT INTO  Life(name,date) VALUES ('{0}', {1})'''.format(st, date)
    cur.execute('''INSERT INTO  Life(name,date) VALUES ('{0}', {1})'''.format(st, date))
    con.commit()


def sqlite_get_stat(left, right):
    mas = []
    for row in cur.execute('SELECT * FROM LIFE WHERE date >{0} and date <{1}'.format(left, right)):
        mas.append([row[2], row[1]])
    mas = sorted(mas, key=lambda x: x[0])
    stat = ''
    for i in mas:
        stat += human_time(i[0]).split(' ')[1]+'  ' + i[1]+'\n'
    return stat
