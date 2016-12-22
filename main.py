# -*- coding: utf-8 -*-


from diary_proto import Diary
from bot_proto import *

BOT_MODE = 0


def check_updates():
    parametersList = telebot.get_updates()
    if not parametersList:
        return
    for parameters in parametersList:
        run_command(*parameters)


def run_command(name, from_id, cmd, author_id):
    global BOT_MODE
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
        telebot.send_text(from_id, 'Pig is '+random.choice(PIG_LIST))  # Answer



    elif re.match(PATTERN_DICE, cmd) is not None:
        number = int(cmd.split('d')[0][1:])
        dice_size = int(cmd.split('d')[1])
        if dice_size < 2 or number < 1:
                telebot.send_text(from_id, '%s, wrong input :C' % name)
                return
        telebot.send_text(from_id, "Result: " + str([random.randint(1, dice_size) for i in range(number)]))

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
            check_updates()
            time.sleep(telebot.Interval)
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
