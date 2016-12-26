import sqlite3
import datetime
con = sqlite3.connect('data/life/life.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS `Life`
            (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
            `name` VARCHAR(100),
            `date` INTEGER);''')

def human_time(time):
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

def sqlite_add(st,date):
    print '''INSERT INTO  Life(name,date) VALUES ('{0}', {1})'''.format(st, date)
    cur.execute('''INSERT INTO  Life(name,date) VALUES ('{0}', {1})'''.format(st, date))
    con.commit()
