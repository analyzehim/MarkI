from bot_proto import *
import os
import time

CHECK_INTERVAL = 20*60

while(True):
    f = open("log.txt", "r")
    last_line = ''
    for line in f:
        last_line = line
    f.close()
    if 'Finish by user' in last_line:
        log_event("FORCE START BY AUTORUNNER")
        os.system('python main.py')
    time.sleep(CHECK_INTERVAL)
