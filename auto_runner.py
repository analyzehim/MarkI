from bot_proto import *
from common_proto import *
import os
import time



while(True):
    f = open("log.txt", "r")
    last_line = ''
    for line in f:
        last_line = line
    f.close()
    if 'Finish by user' in last_line:
        log_event("FORCE START BY AUTORUNNER")
        os.system('python main.py')
    else:
        print "OK, time: {0}".format(human_time(time.time()))
    CHECK_INTERVAL = getHeartBeatInterval()
    time.sleep(CHECK_INTERVAL)
