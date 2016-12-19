# -*- coding: utf-8 -*-
import requests
import time
import subprocess
import os

import random
import re
from diary_proto import Diary
from bot_proto import *
from bot_const import *

MODE = 0

def check_updates():
    global offset
    data = {'offset': offset + 1, 'limit': 5, 'timeout': 0}
    
    try:
        request = requests.post(URL + TOKEN + '/getUpdates', data=data)
    except:
        log_event('Error getting updates')
        return False
    if not request.status_code == 200: return False

    if not request.json()['ok']: return False
    
    for update in request.json()['result']:
        offset = update['update_id']

        if not 'message' in update or not 'text' in update['message']: continue

        from_id = update['message']['chat']['id'] # Chat ID
        author_id = update['message']['from']['id'] # Creator ID
        message = update['message']['text'] 
        try:
            name = update['message']['chat']['first_name']   
        except:
            name = update['message']['from']['first_name'] 

        parameters = (offset, name, from_id, message, author_id)
        try:
            log_event('Message (id%s) from %s (id%s): "%s" with author: %s' % parameters) 
        except:
            pass
        print parameters
        run_command(*parameters)


def run_command(offset, name, from_id, cmd, author_id):
    global MODE
    if cmd == '/ping':
        send_text(from_id, 'pong') 

    elif cmd == '/help':
        send_text(from_id, 'No help today. Sorry, %s'%name)

    elif cmd in ('Hello','hello','hi','Hi'): # Say hello
        send_text(from_id, 'Hello, %s'%name)
        
    elif cmd[0:2] == '/d' and author_id in (ADMIN_ID, PIG_ID):
        d = Diary()
        if cmd == '/d':
            send_text_withKeyboard(from_id,1,[["Day"],["Week"],["Backlog"],["All"]])
        else:
            op = cmd.split(' ')[1]
            if op =='-':
                task_type = int(cmd.split(' ')[2])
                task_id = int(cmd.split(' ')[3])
                print task_id, task_type
                d.delete_id(task_type, task_id)
                output = unicode(str(d.return_list(task_type)), "CP1251")
                send_text(from_id, output)
                return
            if op =='+':
                task_type = int(cmd.split(' ')[2])
                task = cmd.split(' ',3)[3]
                d.add_line(task_type,task.encode('CP1251'))
                output = unicode(str(d.return_list(task_type)), "CP1251")
                send_text(from_id, output)
        MODE = 1
        return
            
        
    elif cmd == '/pig' and author_id in (ADMIN_ID, PIG_ID): 
        send_text(from_id, 'Pig is '+random.choice(PIG_LIST)) # Answer



    elif re.match(PATTERN_DICE,cmd) is not None:
        number = int( cmd.split('d') [0] [1:] )
        dice_size = int( cmd.split('d') [1] )
        if dice_size < 2 or number < 1:
                send_text(from_id, '%s, wrong input :C' %name)
                return
        print 1
        send_text(from_id, "Result: " + str( [ random.randint(1,dice_size) for i in range(number) ] ) )

    elif (MODE == 1):
        d = Diary()
        if cmd =='Day':
             output = unicode(str(d.return_list(0)), "CP1251")
             send_text(from_id, output)
        if cmd =='Week':
             output = unicode(str(d.return_list(1)), "CP1251")
             send_text(from_id, output)
        if cmd =='Backlog':
             output = unicode(str(d.return_list(2)), "CP1251")
             send_text(from_id, output)
        if cmd =='All':
             output = unicode(str(d), "CP1251")
             send_text(from_id, output)
        MODE = 0 
    else:
        MODE = 0

        pass


if __name__ == "__main__":
    while True:
        try:
            check_updates()
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
