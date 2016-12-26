# -*- coding: utf-8 -*-



import sys
import re
sys.path.insert(0, sys.path[0]+'\\proto')

from diary_proto import *
from bot_proto import *
import time
from sqlite_proto import *

'''
BOT_MODE
0 - standart
1 - wait to diary
2 - quiz
3 - life
'''
BOT_MODE = 0
EXIT_MODE = False

def check_updates():
    parametersList = telebot.get_updates()
    if EXIT_MODE == True:
        return 1
    if not parametersList:
        return 0
    for parameters in parametersList:
        run_command(*parameters)


def run_command(name, from_id, cmd, author_id, date):
    global BOT_MODE
    global EXIT_MODE
    if cmd == '/ping':
        telebot.send_text(from_id, 'pong') 

    elif cmd == '/help':
        telebot.send_text(from_id, 'No help today. Sorry, %s' % name)

    elif cmd in ('Hello', 'hello', 'hi', 'Hi'):   # Say hello
        telebot.send_text(from_id, 'Hello, %s' % name)
        
    elif cmd[0:2] == '/d' and author_id in (ADMIN_ID, PIG_ID):
        d = Diary()
        if cmd == '/d':
            telebot.send_text_with_keyboard(from_id, 1, [["Day"], ["Week"], ["Backlog"], ["All"]])
        else:
            op = cmd.split(' ')[1]
            if op == '-':
                task_type = int(cmd.split(' ')[2])
                task_id = int(cmd.split(' ')[3])
                print task_id, task_type
                d.delete_id(task_type, task_id)
                output = unicode(str(d.return_list(task_type)), "CP1251")
                telebot.send_text(from_id, output)
                return
            if op == '+':
                task_type = int(cmd.split(' ')[2])
                task = cmd.split(' ', 3)[3]
                d.add_line(task_type, task.encode('CP1251'))
                output = unicode(str(d.return_list(task_type)), "CP1251")
                telebot.send_text(from_id, output)
        BOT_MODE = 1
        return
            
        
    elif cmd == '/pig' and author_id in (ADMIN_ID, PIG_ID):
        import random
        telebot.send_text(from_id, 'Pig is '+random.choice(PIG_LIST))  # Answer
    elif cmd[0:5] == '/life':
        if len(cmd) == 5:
            BOT_MODE = 3
            telebot.send_text_with_keyboard(from_id, 'Options:',
                                            [["wake up","go sleep"],
                                             ["breakfast","lunch","dinner"],
                                             ["go on work", "go from work"],
                                             ["shower","toilet_B","toilet_S"]])
        else:
            sqlite_add(cmd[6:], date)
            telebot.send_text(from_id, "{0}: {1}".format(cmd[6:], human_time(date)))




    elif re.match(PATTERN_DICE, cmd) is not None:
        import random
        number = int(cmd.split('d')[0][1:])
        dice_size = int(cmd.split('d')[1])
        if dice_size < 2 or number < 1:
                telebot.send_text(from_id, '%s, wrong input :C' % name)
                return
        telebot.send_text(from_id, "Result: " + str([random.randint(1, dice_size) for i in range(number)]))
    elif cmd == '/exit':
        telebot.send_text(from_id, "Finish by user")
        EXIT_MODE = True

    elif BOT_MODE == 3:
        sqlite_add(cmd, date)
        telebot.send_text(from_id, "{0}: {1}".format(cmd, human_time(date)))
        BOT_MODE = 0

    elif BOT_MODE == 1:
        d = Diary()
        if cmd == 'Day':
            output = unicode(str(d.return_list(0)), "CP1251")
            telebot.send_text(from_id, output)
        if cmd == 'Week':
            output = unicode(str(d.return_list(1)), "CP1251")
            telebot.send_text(from_id, output)
        if cmd == 'Backlog':
            output = unicode(str(d.return_list(2)), "CP1251")
            telebot.send_text(from_id, output)
        if cmd == 'All':
            output = unicode(str(d), "CP1251")
            telebot.send_text(from_id, output)
        BOT_MODE = 0 
    else:
        log_event('No action')
        BOT_MODE = 0

        pass


if __name__ == "__main__":
    telebot = Telegram()
    while True:
        try:
            
            # telebot.ping()
            if check_updates() != 1:
                time.sleep(telebot.Interval)
            else:
                sys.exit()
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
